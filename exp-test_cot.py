import os
import subprocess

from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import chromadb
from FlagEmbedding import BGEM3FlagModel
from chromadb import Documents, EmbeddingFunction, Embeddings
from experimental_methods import format_bandit, cot_prompt, remove_backticks

device = "cuda"
model_list = ["Qwen2.5-Coder-7B-Instruct", "Qwen2.5-Coder-3B-Instruct", "codegemma-7b-it",
              "deepseek-coder-7b-instruct-v1.5", "CodeLlama-7b-Python-hf"]

bge_model = BGEM3FlagModel('BAAI/bge-m3',
                           use_fp16=True)


class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        embeddings = bge_model.encode(texts, max_length=1024)['dense_vecs']
        return embeddings


emb_fn = MyEmbeddingFunction()

for model_name in model_list:
    model = AutoModelForCausalLM.from_pretrained(f'D:/model/{model_name}/', device_map="auto")
    tokenizer = AutoTokenizer.from_pretrained(f'D:/model/{model_name}/')
    messages = []

    data_name = ['SecurityEval', 'CyberSecEval', 'PromSec', 'SecCodePLT']
    for name in data_name:

        with open(f'experiment/dataset/{name}/bandit_{name}.json', 'r', encoding='utf-8') as file_b:
            data = json.load(file_b)

        client = chromadb.PersistentClient(path="D:/Chroma/CT")
        collection = client.get_collection(name)

        if os.path.exists(f'experiment/{model_name}/{name}/prompt_cot.json'):
            with open(f'experiment/{model_name}/{name}/prompt_cot.json', 'r', encoding='utf-8') as ff:
                try:
                    temp_results = json.load(ff)
                except json.JSONDecodeError:
                    temp_results = []
        else:
            temp_results = []

        for item in data:
            ID = item.get('ID')

            if any(result['id'] == ID for result in temp_results):
                continue

            code = item.get('code')

            print(code)
            print('----------------------------')

            bandit_result = item.get('bandit_result')
            bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()

            search_bug = format_bandit(bandit_result)

            search_exp = collection.query(
                query_embeddings=emb_fn([search_bug]),
                n_results=1  # 返回前 1 个最相似的结果
            )

            meta_data = search_exp['metadatas'][0][0]
            s_cot = meta_data['s_cot']

            prompt = cot_prompt(code, bandit_result, s_cot)


            tot, flag = 1, 0  # tot表示当前迭代次数，flag表示是否修复代码
            fixed_json = []

            while tot <= 5:
                messages = [
                    {"role": "system", "content": "You are a code vulnerability expert. Below is a vulnerable code "
                                                  "snippet along with the results from Bandit security analysis. "
                                                  "Your task is to fix the vulnerabilities and provide the "
                                                  "corrected version of the code."},
                    {"role": "user", "content": prompt}]

                text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                # print(text)

                encoding = tokenizer(text, return_tensors="pt").to(device)

                generated_ids = model.generate(encoding.input_ids, max_new_tokens=2048, do_sample=True)

                generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in
                                 zip(encoding.input_ids, generated_ids)]

                response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

                fixed_json.append(response)

                fix_code = remove_backticks(response)

                with open(ID, "w") as f:
                    f.write(fix_code)

                print(f"正在对 {ID} 进行 Bandit 安全扫描...")

                # 执行 Bandit 测试
                bandit_run = subprocess.run(
                    [r'C:\Users\n\AppData\Roaming\Python\Python311\Scripts\bandit.exe', '-r', ID], capture_output=True,
                    text=True)

                if os.path.exists(ID):
                    os.remove(ID)

                bandit_run = bandit_run.stdout
                # 检查是否有安全问题
                if "No issues identified" not in bandit_run:
                    flag = 1
                else:
                    tot += 1
                    bandit_run = bandit_run.split('Test results:')[1].split('Code scanned:')[0].strip()


                    sub_search_bug = format_bandit(bandit_run)
                    sub_search_exp = collection.query(
                        query_embeddings=emb_fn([sub_search_bug]),
                        n_results=1  # 返回前 1 个最相似的结果
                    )

                    sub_meta_data = sub_search_exp['metadatas'][0][0]
                    sub_s_cot = sub_meta_data['s_cot']
                    prompt = cot_prompt(fix_code, bandit_run, sub_s_cot)

                print(response)
                print('----------------------------')

                if flag:
                    break

            folder_path = f'experiment/{model_name}/{name}/'
            # 检查文件夹是否存在，不存在则创建
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            json_path = f'{folder_path}prompt_cot.json'

            try:
                with open(json_path, 'r', encoding='utf-8') as file_j:
                    save_data = json.load(file_j)
            except (FileNotFoundError, json.JSONDecodeError):
                save_data = []  # 如果文件不存在或为空，则初始化为空列表

            # 将新数据追加到列表中
            save_data.append({"id": ID, "fixed_list": fixed_json, "flag": str(flag)})

            # 重新写回文件
            with open(json_path, 'w', encoding='utf-8') as file_j:
                json.dump(save_data, file_j, ensure_ascii=False, indent=4)



