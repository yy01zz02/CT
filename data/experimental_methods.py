def reasoning_fix(block: str, block_above: str, block_below: str, info: str) -> str:
    res = f"""The following is the vulnerable code. The vulnerable code block is surrounded by '```'
{block_above}
```
{block}
```
{block_below}

Vulnerability information:{info}
Please provide a fixed version of the vulnerable code block. Your reply should only contain the fixed code block, that is, you only need to modify the code blocks surrounded by ``` and do not output anything else!!!
"""
    return res


def prompt_not_content(block: str, info: str) -> str:
    res = f"""The following is the vulnerable code. The vulnerable code block is surrounded by '```'
```
{block}
```

Vulnerability information:{info}
Please provide a fixed version of the vulnerable code block. Your reply should only contain the fixed code block, that is, you only need to modify the code blocks surrounded by ``` and do not output anything else!!!
"""
    return res


def cot_prompt(block: str, block_above: str, block_below: str, info: str, example_cot: str) -> str:
    res = f"""The following is the vulnerable code. The vulnerable code block is surrounded by '```'
{block_above}
```
{block}
```
{block_below}

Vulnerability information:{info}
In addition, the following vulnerability repair COT examples are provided for reference. 
If the similarity with the vulnerability code is too low, do not refer to it:

{example_cot}

Please provide a fixed version of the vulnerable code block. Your reply should only contain the fixed code block, that is, you only need to modify the code blocks surrounded by ``` and do not output anything else!!!
"""
    return res


def cot_prompt_not_content(block: str, info: str, example_cot: str) -> str:
    res = f"""The following is the vulnerable code. The vulnerable code block is surrounded by '```'
```
{block}
```
Vulnerability information:{info}
In addition, the following vulnerability repair COT examples are provided for reference. 
If the similarity with the vulnerability code is too low, do not refer to it:

{example_cot}

Please provide a fixed version of the vulnerable code block. Your reply should only contain the fixed code block, that is, you only need to modify the code blocks surrounded by ``` and do not output anything else!!!
"""
    return res


def simplify_cot_1(cot: str) -> str:
    res = f"""In your summary:
1. Identify the key vulnerabilities and their root causes.
2. Highlight the main solutions or fixes proposed to address the vulnerabilities.
3. Focus only on the most relevant details, leaving out extraneous information and excessive code.
4. Try to keep your summary under 100 words and make sure it applies to similar vulnerabilities.
5. Output should not include formatting or code examples!!!

The goal is to provide a generalizable, actionable chain of thought that can be referenced for similar code vulnerability situations.
Provide a clear and concise summary of the following Chain of Thought (COT) related to vulnerability analysis:
```
{cot}
```
"""
    return res


def simplify_cot(cot: str) -> str:
    res = f"""Simplify the following chain of thought into a concise, actionable summary with these steps:
1. Identify the key vulnerabilities and their root causes.
2. Outline the main solutions or fixes proposed to address the vulnerabilities.
3. Focus only on essential details—exclude extraneous information and code examples.
Ensure the summary is under 200 words and formatted strictly as a numbered list (e.g., 1. 2. 3.). Do not include any formatting or code snippets in the output.

Chain of Thought:
{cot}
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
