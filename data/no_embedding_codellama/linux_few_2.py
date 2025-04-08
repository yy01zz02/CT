import os
import subprocess

from transformers import AutoModelForCausalLM, AutoTokenizer
import json


from experimental_methods import few_2, remove_backticks
import os
current_file_path = __file__
f_name = os.path.basename(current_file_path).split('.')[0]

device = "cuda"
model_list = ["/root/.cache/modelscope/hub/models/AI-ModelScope/CodeLlama-7b-Instruct-hf"]

vers = "2"


for model_path in model_list:
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    messages = []

    model_name = model_path.split('/')[-1]

    data_names = ['CyberSecEval', 'PromSec', 'SecCodePLT', 'SecurityEval']
    for name in data_names:

        # 漏洞数据集
        with open(f'../{name}/{name}_cot_{vers}.json', 'r', encoding='utf-8') as file_b:
            data = json.load(file_b)

        prompt_file = f'../exp/{model_name}/{name}/{f_name}.json'
        # 读取已经处理过的数据
        if os.path.exists(prompt_file):
            with open(prompt_file, 'r', encoding='utf-8') as ff:
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

            meta_data_0 = item.get('meta_data_0')
            exp_bug_0 = item.get('exp_bug_0')
            fixed_code_0 = meta_data_0['fixed_code']

            meta_data_1 = item.get('meta_data_1')
            exp_bug_1 = item.get('exp_bug_1')
            fixed_code_1 = meta_data_1['fixed_code']

            prompt = few_2(bug, exp_bug_0, fixed_code_0, exp_bug_1, fixed_code_1)

            print(f'{model_name}-----{name}-----{id}')

            flag = 0  # tot表示当前迭代次数，flag表示是否修复代码
            prompt = f"<s>[INST] {prompt} [/INST]"

            while True:
                encoding = tokenizer(prompt, return_tensors="pt").to(device)
                generated_ids = model.generate(
                    encoding.input_ids,
                    max_new_tokens=256,
                    do_sample=True,
                    eos_token_id=tokenizer.eos_token_id,
                    temperature=0.7
                )
                response = tokenizer.decode(generated_ids[0][len(prompt) - 1:], skip_special_tokens=True)

                fix_code = remove_backticks(response)
                if fix_code.strip() != "":
                    break

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

            print(response)
            print('----------------------------')

            folder_path = f'../exp/{model_name}/{name}/'
            # 检查文件夹是否存在，不存在则创建
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # 保存结果路径
            json_path = f'{folder_path}{f_name}.json'

            try:
                with open(json_path, 'r', encoding='utf-8') as file_j:
                    save_data = json.load(file_j)
            except (FileNotFoundError, json.JSONDecodeError):
                save_data = []  # 如果文件不存在或为空，则初始化为空列表

            # 将新数据追加到列表中
            save_data.append({"id": id, "fixed_code": fix_code, "flag": str(flag)})

            # 重新写回文件
            with open(json_path, 'w', encoding='utf-8') as file_j:
                json.dump(save_data, file_j, ensure_ascii=False, indent=4)

    del model
    del tokenizer

