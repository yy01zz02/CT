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




def reasoning_fix(block: str) -> str:
    res = f"""The current task is to fix the vulnerable code snippet below.
```
{block}
```
"""
    return res


def cot_prompt(block: str, example_cot: str) -> str:
    res = f"""Below is an example of a vulnerability code snippet fix.
Steps to fix similar vulnerability code snippets:
```
{example_cot}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```
"""
    return res


def oneshot_prompt(block: str, example_bug: str, example_fix: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
Example vulnerability code snippet:
```
{example_bug}
```
Example fixed code snippet:
```
{example_fix}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```
"""
    return res
