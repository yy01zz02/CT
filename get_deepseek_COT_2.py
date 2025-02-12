import json
import os
import requests
import time


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
        "max_tokens": 8192,
    }
    headers = {
        "Authorization": "Bearer sk-iewubqewnuedfxzlkyioxkvbnxnbsuenonbhrjffdbnvgdli",
        "Content-Type": "application/json"
    }

    for attempt in range(100):  # 最多重试100次
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # 检查HTTP错误
            return response.text
        except requests.RequestException as e:
            print(f"请求失败，重试 {attempt + 1}/100: {e}")
            time.sleep(10)  # 休眠5秒后重试

    raise Exception("连续100次请求失败，程序终止。")


file_path = 'data/PromSec/bandit/bandit_PromSec_fixed_7.json'
save_path = 'data/PromSec/deepseek_PromSec_fixed_7.json'

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
        ID = entry['ID']
        code = entry['code']
        bandit_result = entry['bandit_result']
        bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()

        if any(result['ID'] == ID for result in results):
            continue

        prompt = f"""
        You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

        Vulnerable Code:
        {code}

        Bandit Analysis Results:
        {bandit_result}

        Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
        """

        content = get_text(prompt)

        result = {
            "ID": ID,
            "content": content
        }

        results.append(result)

        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"ID {ID} 的结果已保存。")

    except Exception as e:
        error_count += 1
        print(f"处理 ID {entry['ID']} 时发生错误（错误次数: {error_count}）：{e}")
        if error_count >= 100:
            print("错误次数达到100次，程序终止。")
            break

print("所有结果已保存到文件中")
