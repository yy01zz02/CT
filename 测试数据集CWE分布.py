import json
from collections import Counter

# 读取JSON文件
with open('data/CyberSecEval/CyberSecEval_final.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

cwe_count = Counter()

# 迭代列表中的每个字典，提取cwe_list
for entry in data:
    cwe_list = entry.get('cwe_list', [])
    cwe_count.update(cwe_list)

# 打印结果
tot = 0
for cwe, count in cwe_count.items():
    # print(count)
    print(f'CWE {cwe}: {count}')
    tot += 1
# print(len(data))
print(f'Total CWE count: {tot}')
