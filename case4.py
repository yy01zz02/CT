import json


# 读取JSON文件
with open('data/SecCodePLT/SecCodePLT_final.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for entry in data:
    buggy_code = entry['buggy_code']
    bandit_result = entry['bandit_result']
    fixed_code = entry['fixed_code']
    reasoning_content = entry['reasoning_content']
    cwe_list = entry['cwe_list']
    simplify_cot = entry['simplify_cot']

    print(bandit_result)

    break