import json
from collections import Counter


# 读取JSON文件
def count_cwe_numbers(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 假设 JSON 是一个包含多个对象的列表
    cwe_numbers = [item.get('cwe_number') for item in data if 'cwe_number' in item]

    # 统计每个 "cwe_number" 的出现次数
    cwe_count = Counter(cwe_numbers)

    return cwe_count


# 使用示例
json_file = 'experiment/dataset/CyberSecEval/CyberSecEval_Database.json'  # 替换为你的JSON文件路径
result = count_cwe_numbers(json_file)


tot = 0
for cwe, count in result.items():
    # print(son'cwe_number: {cwe}, count: {count}')
    tot += 1

print(f'Total CWE count: {tot}')


json_file = 'experiment/dataset/PromSec/PromSec_Database.json'  # 替换为你的JSON文件路径
result = count_cwe_numbers(json_file)


tot = 0
for cwe, count in result.items():
    # print(son'cwe_number: {cwe}, count: {count}')
    tot += 1

print(f'Total CWE count: {tot}')

json_file = 'experiment/dataset/SecCodePLT/SecCodePLT_Database.json'  # 替换为你的JSON文件路径
result = count_cwe_numbers(json_file)


tot = 0
for cwe, count in result.items():
    # print(son'cwe_number: {cwe}, count: {count}')
    tot += 1

print(f'Total CWE count: {tot}')

json_file = 'experiment/dataset/SecurityEval/SecurityEval_Database.json'  # 替换为你的JSON文件路径
result = count_cwe_numbers(json_file)


tot = 0
for cwe, count in result.items():
    # print(son'cwe_number: {cwe}, count: {count}')
    tot += 1

print(f'Total CWE count: {tot}')
