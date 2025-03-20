import os
import subprocess

from transformers import AutoModelForCausalLM, AutoTokenizer
import json

from experimental_methods import reasoning_fix, remove_backticks

device = "cuda"
model_list = ["/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-Coder-7B-Instruct-AWQ",
              # "/root/.cache/modelscope/hub/models/TheBloke/CodeLlama-70B-hf-AWQ",
              "/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4"]

vers = "2"

for model_path in model_list:
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    messages = []

    model_name = model_path.split('/')[-1]

    data_names = ['SecurityEval', 'CyberSecEval', 'PromSec', 'SecCodePLT']
    for name in data_names:

        # 漏洞数据集
        with open(f'../{name}/{name}_{vers}.json', 'r', encoding='utf-8') as file_b:
            data = json.load(file_b)

        # 读取已经处理过的数据
        if os.path.exists(f'../exp/{model_name}/{name}/prompt_not_cot.json'):
            with open(f'../exp/{model_name}/{name}/prompt_not_cot.json', 'r', encoding='utf-8') as ff:
                try:
                    temp_results = json.load(ff)
                except json.JSONDecodeError:
                    temp_results = []
        else:
            temp_results = []

        for item in data:
            id = item.get('id')

            if any(result['id'] == id for result in temp_results):
                continue

            bug = item.get('bug')
            bug_before = item.get('bug_before')
            bug_after = item.get('bug_after')
            issue = item.get('issue')

            prompt = reasoning_fix(bug, issue)

            pre = "You are a code vulnerability expert.\n"

            prompt = pre + prompt

            print(prompt)
            print('----------------------------')

            tot, flag = 1, 0  # tot表示当前迭代次数，flag表示是否修复代码
            fix = ''
            messages = [{"role": "user", "content": prompt}]

            while tot <= 5:

                text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                # print(text)

                encoding = tokenizer(text, return_tensors="pt").to(device)

                generated_ids = model.generate(encoding.input_ids, max_new_tokens=2048, do_sample=True)

                generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in
                                 zip(encoding.input_ids, generated_ids)]

                response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

                messages.append({"role": "assistant", "content": response})

                fix_code = remove_backticks(response)
                fix = response

                with open(id, "w", encoding='utf-8') as f:
                    f.write(fix_code)

                print(f"正在对 {id} 进行 Bandit 安全扫描...")

                # 执行 Bandit 测试
                bandit_run = subprocess.run(
                    [r'bandit', '-r', id], capture_output=True,
                    text=True)

                if os.path.exists(id):
                    os.remove(id)

                bandit_run = bandit_run.stdout
                # 检查是否有安全问题
                if "No issues identified" not in bandit_run:
                    flag = 1
                else:
                    tot += 1
                    br = bandit_run.split('Test results:')[1].split('Code scanned:')[0].strip()

                    prompt = (f"Your previous response was not accepted. Please try again.\n"
                              f"The vulnerability analysis is as follows:\n{br}"
                              f"Your reply should only contain the fixed code block!!!")
                    messages.append({"role": "user", "content": prompt})

                print(response)
                print('----------------------------')

                if flag:
                    break

            folder_path = f'../exp/{model_name}/{name}/'
            # 检查文件夹是否存在，不存在则创建
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # 保存结果路径
            json_path = f'{folder_path}prompt_not_cot.json'

            try:
                with open(json_path, 'r', encoding='utf-8') as file_j:
                    save_data = json.load(file_j)
            except (FileNotFoundError, json.JSONDecodeError):
                save_data = []  # 如果文件不存在或为空，则初始化为空列表

            # 将新数据追加到列表中
            save_data.append({"id": id, "fixed_code": fix, "flag": str(flag), "fix_count": tot})

            # 重新写回文件
            with open(json_path, 'w', encoding='utf-8') as file_j:
                json.dump(save_data, file_j, ensure_ascii=False, indent=4)
