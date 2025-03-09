import json
import re
from collections import defaultdict

names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]
mp = defaultdict(int)

for name in names:
    file_path = f"{name}/bandit_{name}.json"
    save_path = f"{name}/block_{name}.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)


    results = []
    cnt = 0
    for entry in data:
        code = entry["code"]
        bandit_result = entry["bandit_result"]

        bandit_result = bandit_result.split('Test results:')[1].split('Code scanned:')[0].strip()
        cwe_list = re.findall(r'CWE-(\d+)(?=[^\w-]|$)', bandit_result)

        bandit_list = bandit_result.split('--------------------------------------------------')

        bandit_list_temp = []
        for bandit in bandit_list:
            if bandit.strip() == "":
                continue
            bandit_list_temp.append(bandit.strip())

        bandit_list = bandit_list_temp

        bandit_list_temp = []
        row_number = []
        issue_list = []

        for bandit in bandit_list:
            bandit_row = bandit.split('\n')
            res, row_list = [], []
            for row in bandit_row:
                if "Issue: " in row:
                    issue_list.append(row.strip().replace(">> Issue: ", ""))

                if (row.strip() == "" or row[2:].strip() == "" or "Issue: " in row or "Severity: " in row or
                        "More Info: " in row or "Location: " in row or "CWE: " in row):
                    continue

                res.append(row[2:])
                row_list.append(int(row[:2]))

            res = '\n'.join(res)
            bandit_list_temp.append(res)
            row_number.append(row_list)

        bandit_list = bandit_list_temp

        bug_before, bug_after = [], []

        for i in range(len(row_number)):
            before = row_number[i][0]
            after = row_number[i][-1]
            code_row = code.split('\n')

            bug_before.append('\n'.join(code_row[:before - 1]))
            bug_after.append('\n'.join(code_row[after:]))

        for i in range(len(bandit_list)):
            if mp[bandit_list[i]] > 0:
                continue

            mp[bandit_list[i]] = 1
            results.append({
                "id": f'{name}_{cnt}',
                "bug": bandit_list[i],
                "bug_before": bug_before[i],
                "bug_after": bug_after[i],
                "cwe": cwe_list[i],
                "issue": issue_list[i]
            })
            cnt += 1

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f'{name}:{cnt}')




