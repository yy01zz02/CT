import json

with open("experiment/dataset/SecCodePLT/SecCodePLT_RAG.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    bandit_result = item['bandit_result']

    single_bandit_list = bandit_result.split('--------------------------------------------------')

    for single_bandit in single_bandit_list:
        if single_bandit == '':
            continue

        single_bandit_row_list = single_bandit.split('\n')
        res = []
        for row in single_bandit_row_list:
            if (row.strip() == "" or row[2:].strip() == "" or "Issue: " in row or "Severity: " in row or
                    "More Info: " in row or "Location: " in row or "CWE: " in row):
                continue

            res.append(row[2:])

        res = '\n'.join(res)

        print(res)

        print('--------------------------------------------------')
