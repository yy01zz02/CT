import json
from collections import Counter


names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]
tot_data = []
for name in names:
    path = f'{name}/{name}.json'

    # 读取 JSON 文件
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tot_data.extend(data)

    # 提取所有的 "cwe" 字段
    cwe_values = [item.get('cwe') for item in data if item.get('cwe')]

    # 使用 Counter 来统计每个 "cwe" 出现的次数
    cwe_count = Counter(cwe_values)

    # 按照 cwe 编号升序排序
    sorted_cwe_count = sorted(cwe_count.items(), key=lambda x: int(x[0]))

    # 输出排序后的统计结果\
    cnt, cnt2 = 0, 0
    print(f"数据集 {name}")
    for cwe, count in sorted_cwe_count:
        print(f"CWE-{cwe}: {count} 次")
        cnt += count
        cnt2 += 1

    print(f"Total: {cnt} 次, {cnt2} 个 CWE")

    print('--------------------------------')

# 提取所有的 "cwe" 字段
cwe_values = [item.get('cwe') for item in tot_data if item.get('cwe')]

# 使用 Counter 来统计每个 "cwe" 出现的次数
cwe_count = Counter(cwe_values)

# 按照 cwe 编号升序排序
sorted_cwe_count = sorted(cwe_count.items(), key=lambda x: int(x[0]))

# 输出排序后的统计结果\
cnt, cnt2 = 0, 0
print(f"所有数据集")
for cwe, count in sorted_cwe_count:
    print(f"CWE-{cwe}: {count} 次")
    cnt += count
    cnt2 += 1
print(f"Total: {cnt} 次, {cnt2} 个 CWE")

print('--------------------------------')



