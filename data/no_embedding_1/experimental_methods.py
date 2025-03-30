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




def reasoning_fix(block: str, info: str, block_above: str, block_below: str) -> str:
    res = f"""The current task is to fix the vulnerable code block.
    
Complete code:
{block_above}
{block}
{block_below}

Vulnerability information:{info}

Below is the vulnerable code snippet that you need to fix. Your reply should only contain the fixed code snippet. Do not output anything else!!!
```
{block}
```
"""
    return res


def cot_prompt(block: str, info: str, example_cot: str, example_bug: str, example_fix: str, block_above: str,
               block_below: str) -> str:
    example_fix = remove_backticks(example_fix)
    example_bug = remove_backticks(example_bug)
    res = f"""Please refer to the following example to fix the vulnerability:
    
Example vulnerability code snippet is as follows:
```
{example_bug}
```

The repair ideas are as follows:
```
{example_cot}
```

Example fixed code snippet is as follows:
```
{example_fix}
```

The current task is to fix the vulnerable code block.

Complete code:
{block_above}
{block}
{block_below}

Vulnerability information:{info}

Below is the vulnerable code snippet that you need to fix. Your reply should only contain the fixed code snippet. Do not output anything else!!!
```
{block}
```

"""
    return res


def cot_prompt_P(block: str, info: str, example_cot: str, example_bug: str, example_fix: str, block_above: str,
               block_below: str) -> str:
    example_fix = remove_backticks(example_fix)
    example_bug = remove_backticks(example_bug)
    res = f"""Please refer to the following example to fix the vulnerability:

The repair ideas are as follows:
```
{example_cot}
```

Example vulnerability code snippet is as follows:
```
{example_bug}
```

Example fixed code snippet is as follows:
```
{example_fix}
```

The current task is to fix the vulnerable code block.

Complete code:
{block_above}
{block}
{block_below}

Vulnerability information:{info}

Below is the vulnerable code snippet that you need to fix. Your reply should only contain the fixed code snippet. Do not output anything else!!!
```
{block}
```

"""
    return res



def oneshot_prompt(block: str, info: str, example_bug: str, example_fix: str, block_above: str,
                   block_below: str) -> str:
    example_fix = remove_backticks(example_fix)
    example_bug = remove_backticks(example_bug)
    res = f"""Please refer to the following example to fix the vulnerability:
    
Example vulnerability code snippet is as follows:
```
{example_bug}
```

Example fixed code snippet is as follows:
```
{example_fix}
```

The current task is to fix the vulnerable code block.

Complete code:
{block_above}
{block}
{block_below}

Vulnerability information:{info}

Below is the vulnerable code snippet that you need to fix. Your reply should only contain the fixed code snippet. Do not output anything else!!!
```
{block}
```
"""
    return res
