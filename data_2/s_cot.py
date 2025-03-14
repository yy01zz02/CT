import json
import os
import requests
import time
from experimental_methods import simplify_cot


def get_text(message):
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        # "model": "Pro/deepseek-ai/DeepSeek-R1",
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": message,
        "max_tokens": 8192,
    }
    headers = {
        "Authorization": "Bearer sk-gsvdwjiwudoaahhxfjzatwelubmjivmpdeaabburjeysbvel",
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


names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]
for name in names:


# name = "SecurityEval"

    file_path = f'{name}/fixed_sorted_{name}.json'
    save_path = f'dataset/simplify_{name}_1.json'

    # 读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    results = []
    error_count = 0

    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='utf-8') as ff:
            try:
                results = json.load(ff)
            except json.JSONDecodeError:
                results = []
    else:
        results = []

    # 处理每一条数据
    for entry in data:
        try:
            id = entry['id']

            if any(temp_result['id'] == id for temp_result in results):
                continue

            cot = entry['cot']

            messages = [
                {
                    "role": "system",
                    "content": "You are an AI assistant that helps to extract key points from a Chain of Thought (COT) "
                               "focused on vulnerability fixes. Your task is to identify the primary issues related to "
                               "the vulnerability and the proposed solutions, summarizing these into a clear and concise "
                               "format suitable for similar vulnerability fixes. Keep the summary under 200 words, "
                               "and ensure it is actionable and relevant for similar situations."
                }
            ]

            prompt = simplify_cot(cot)

            messages.append({"role": "user", "content": prompt})

            print(id)
            print(prompt)
            print()

            text = get_text(messages)
            parsed_data = json.loads(text)
            s_cot = parsed_data["choices"][0]["message"]["content"]

            result = {
                "id": id,
                "cot": cot,
                "s_cot": s_cot
            }

            results.append(result)

            with open(save_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=4)

            print(f"ID {id} 的结果已保存。")

        except Exception as e:
            error_count += 1
            print(f"处理 ID {entry['id']} 时发生错误（错误次数: {error_count}）：{e}")
            if error_count >= 100:
                print("错误次数达到100次，程序终止。")
                break
