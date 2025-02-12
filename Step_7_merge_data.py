import os
import json
import re


# 读取第一个 JSON 文件
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


file1_path = "data/SecCodePLT/bandit_SecCodePLT.json"
file2_path = "data/SecCodePLT/fixed_and_reason_all.json"
output_path = "data/SecCodePLT/SecCodePLT_data.json"

json_data1 = load_json(file1_path)
json_data2 = load_json(file2_path)

# 将数据按 ID 进行匹配
merged_results = []
lookup = {entry['ID']: entry for entry in json_data2}

for entry in json_data1:
    ID = entry['ID']
    fixed_code = lookup.get(ID, {}).get("Fixed_code", "")
    reasoning_content = lookup.get(ID, {}).get("reasoning_content", "")
    bandit_result = entry['bandit_result']
    bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()

    cwe_numbers = re.findall(r'CWE-(\d+)(?=[^\w-]|$)', bandit_result)
    cwe_numbers = [int(cwe) for cwe in cwe_numbers]

    merged_results.append({
        "id": ID,
        "buggy_code": entry["code"],
        "bandit_result": bandit_result,
        "fixed_code": fixed_code,
        "reasoning_content": reasoning_content,
        "cwe_list": cwe_numbers
    })



with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(merged_results, f, ensure_ascii=False, indent=4)

print("合并完成，结果已保存到:", output_path)
