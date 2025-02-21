import json
import re
from collections import defaultdict

file_path = "dataset/PromSec/PromSec_RAG.json"
save_path = "dataset/PromSec/PromSec_Database.json"

# file_path = "dataset/CyberSecEval/CyberSecEval_RAG.json"
# save_path = "dataset/CyberSecEval/CyberSecEval_Database.json"
#
# file_path = "dataset/SecCodePLT/SecCodePLT_RAG.json"
# save_path = "dataset/SecCodePLT/SecCodePLT_Database.json"
#
# file_path = "dataset/SecurityEval/SecurityEval_RAG.json"
# save_path = "dataset/SecurityEval/SecurityEval_Database.json"


# 读取JSON文件
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

mp = defaultdict(int)
Rag_data = []
cnt = 0


for entry in data:
    buggy_code = entry['buggy_code']
    bandit_result = entry['bandit_result']
    fixed_code = entry['fixed_code']
    reasoning_content = entry['reasoning_content']
    cwe_list = entry['cwe_list']
    s_cot = entry['s_cot']

    single_bandit_list = bandit_result.split('--------------------------------------------------')

    for single_bandit in single_bandit_list:
        if single_bandit == '':
            continue

        match = re.search(r'CWE:\s*CWE-(\d+)', single_bandit)
        cwe_number = int(match.group(1))
        print(cwe_number)

        single_bandit_row_list = single_bandit.split('\n')
        res = []
        for row in single_bandit_row_list:
            if (row.strip() == "" or row[2:].strip() == "" or "Issue: " in row or "Severity: " in row or
                    "More Info: " in row or "Location: " in row or "CWE: " in row):
                continue
            res.append(row[2:])

        res = '\n'.join(res)
        print(res)
        cnt += 1
        print('--------------------------------------------------')
        if mp[res] == 1:
            continue

        Rag_data.append({
            "block": res,
            "buggy_code": buggy_code,
            "fixed_code": fixed_code,
            "reasoning_content": reasoning_content,
            "s_cot": s_cot,
            "cwe_number": cwe_number
        })
        mp[res] = 1

print(cnt)
print(len(Rag_data))

with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(Rag_data, f, ensure_ascii=False, indent=4)

