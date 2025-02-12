import json
import os
import requests
import time


def get_text(text):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ],
        "stream": False,
        "max_tokens": 4096,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
        "tools": [
            {
                "type": "function",
                "function": {
                    "description": "<string>",
                    "name": "<string>",
                    "parameters": {},
                    "strict": False
                }
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-tytzlnwnhvhppbqrvkffegcbzscnpjzylklukzqsuvpvinap",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

    for attempt in range(100):  # 最多重试100次
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # 检查HTTP错误
            return response.text
        except requests.RequestException as e:
            print(f"请求失败，重试 {attempt + 1}/100: {e}")
            time.sleep(10)  # 休眠5秒后重试

    raise Exception("连续100次请求失败，程序终止。")


file_path = 'data/PromSec/PromSec_data.json'
save_path = 'data/PromSec/PromSec_data_simplify.json'

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# 读取现有的文件内容，确保是一个有效的 JSON 数组格式
if os.path.exists(save_path):
    with open(save_path, 'r', encoding='utf-8') as f:
        try:
            results = json.load(f)
        except json.JSONDecodeError:
            results = []
else:
    results = []

error_count = 0

# 处理每一条数据
for entry in data:
    try:
        ID = entry['id']
        if any(result['id'] == ID for result in results):
            continue

        reasoning_content = entry['reasoning_content']

        prompt = f"""
        I will provide a detailed reasoning process for the model to address the code vulnerability. 
        Please generate a simplified and well-structured version of the Chain of Thought (COT). For example:
        1. First, identify the main issue.
        2. Next, break down the problem into smaller, manageable components.
        3. Then, apply the most suitable method to resolve each component.
        (There may be additional intermediate steps involved.)
        
        Your response should only contain COT, no other content, and should be within 500 words!!!
        Here is the original COT provided by the reasoning model:
        {reasoning_content}
        """

        content = get_text(prompt)

        result = {
            "id": entry['id'],
            "buggy_code": entry['buggy_code'],
            "bandit_result": entry['bandit_result'],
            "fixed_code": entry['fixed_code'],
            "reasoning_content": entry['reasoning_content'],
            "cwe_list": entry['cwe_list'],
            "simplify_cot": content
        }

        results.append(result)

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"ID {ID} 的结果已保存。")

    except Exception as e:
        error_count += 1
        print(f"处理 ID {entry['id']} 时发生错误（错误次数: {error_count}）：{e}")
        if error_count >= 100:
            print("错误次数达到100次，程序终止。")
            break

print("所有结果已保存到文件中")
