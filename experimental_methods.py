import csv
import os


def format_bandit(bandit_result) -> str:
    single_bandit_list = bandit_result.split('--------------------------------------------------')
    block_list = []
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
        block_list.append(res)

    return '\n'.join(block_list)


def normal_fix(buggy_code: str, bandit_result: str) -> str:
    res = f"""Vulnerable Code:
```
{buggy_code}
```
Bandit Analysis Results:
```
{bandit_result}
```
Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
"""
    return res



def cot_prompt(buggy_code: str, bandit_result: str, example_cot: str) -> str:
    res = f"""Vulnerable code: 
```
{buggy_code}
```
Bandit analysis result: 
```
{bandit_result} 
```
In addition, the following vulnerability repair COT examples are provided for reference. 
If the similarity with the vulnerability code is too low, do not refer to it:
```
{example_cot}
```
Please apply this guidance to fix the vulnerability in the provided code. Your response should only contain code, do not output anything else!!!
"""
    return res


def remove_backticks(s):
    # 查找第一个```的位置
    start_idx = s.find("```")
    if start_idx != -1:
        # 从第一个```之后开始，查找最后一个```的位置
        end_idx = s.rfind("```")
        if end_idx != -1:
            # 截取从第一个```之后到最后一个```之前的部分
            s = s[start_idx + 3:end_idx]
    return s.replace('python', ' ')






