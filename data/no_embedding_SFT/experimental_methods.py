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




def zeroshot(block: str) -> str:
    res = f"""The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res



