import json
import os

import requests


def get_text(text):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "Pro/deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ],
        # "stream": False,
        "max_tokens": 8192,
        # "stop": ["null"],
        # "temperature": 0.7,
        # "top_p": 1,
        # "top_k": 50,
        # "frequency_penalty": 0,
        # "n": 1,
        # "response_format": {"type": "text"},
        # "tools": [
        #     {
        #         "type": "function",
        #         "function": {
        #             "description": "<string>",
        #             "name": "<string>",
        #             "parameters": {},
        #             "strict": False
        #         }
        #     }
        # ]
    }
    headers = {
        "Authorization": "Bearer sk-iewubqewnuedfxzlkyioxkvbnxnbsuenonbhrjffdbnvgdli",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text


file_path = 'data/SecurityEval/bandit/bandit_SecurityEval_fixed_3.json'
save_path = 'data/SecurityEval/deepseek/deepseek_SecurityEval_fixed_3.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# flag = True

# 处理每一条数据
for entry in data:

    # # 跳过第一条数据
    # if flag:
    #     flag = False
    #     continue

    code = entry['code']
    bandit_result = entry['bandit_result']

    bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()

    # 拼接生成的提示语
    prompt = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable Code:
{code}

Bandit Analysis Results:
{bandit_result}

Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
    """

    # 输出生成的提示语
    # print(prompt)

    content = get_text(prompt)

    result = {
        "ID": entry['ID'],
        "content": content
    }

    # 读取现有的文件内容，确保是一个有效的 JSON 数组格式
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as f:
            try:
                results = json.load(f)  # 尝试加载现有内容
            except json.JSONDecodeError:
                results = []  # 如果文件为空或格式错误，初始化为空数组
    else:
        results = []  # 如果文件不存在，初始化为空数组

    # 将新结果追加到现有数据
    results.append(result)

    # 每次保存数据，确保文件格式是有效的 JSON 数组
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"ID {entry['ID']} 的结果已保存。")
    # break


print("所有结果已保存到文件中")

