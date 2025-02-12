import json
import time

import requests


# 你的 get_text 函数示例
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
        "Authorization": "Bearer sk-mnzjibdvewxythrehjkdskmmeqrcidlztenrqianovzenhki",
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


change_file = 'data/SecCodePLT/deepseek_SecCodePLT.json'
bindit_file = 'data/SecCodePLT/bandit_SecCodePLT.json'

# 读取主 JSON 文件
with open(change_file, 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)

# 读取第二个 JSON 文件
with open(bindit_file, 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)


# 创建一个字典，方便根据 ID 查找 data2.json 中的对应数据
data2_dict = {item['ID']: item for item in data2}

# 处理 data1.json 中的每一条数据
for item in data1:
    content = item.get('content', '')

    # 如果 content 字段中包含 '504'
    if '504 Gateway Time-out' in content:
        # 获取 ID 字段
        item_id = item.get('ID')

        # 在 data2_dict 中查找对应的 ID 数据
        if item_id in data2_dict:
            code = data2_dict[item_id].get('code')
            bandit_result = data2_dict[item_id].get('bandit_result')

            prompt = f"""
            You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

            Vulnerable Code:
            {code}

            Bandit Analysis Results:
            {bandit_result}

            Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
                """

            # 调用 get_text 函数处理 text_value
            new_content = get_text(prompt)

            # 替换当前数据的 content 字段
            item['content'] = new_content

# 保存修改后的 data1.json
with open(change_file, 'w', encoding='utf-8') as file1_out:
    json.dump(data1, file1_out, ensure_ascii=False, indent=4)

print("Data processing completed")
