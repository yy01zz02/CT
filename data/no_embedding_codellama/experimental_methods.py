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


def cot(block: str, example_cot: str) -> str:
    res = f"""Below is an example of a vulnerability code snippet fix.
Steps to fix similar vulnerability code snippets:
```
{example_cot}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res


def cot_fix(block: str, example_cot: str, example_bug: str, example_fix: str) -> str:
    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
{example_bug}
```
{example_fix}
```
Steps to fix similar vulnerability code snippets:
```
{example_cot}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res


def oneshot(block: str, example_bug: str, example_fix: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
<BUG-1>
{example_bug}
<FIXED-1>
{example_fix}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res


def few_2(block: str, example_bug: str, example_fix: str, example_bug_1: str, example_fix_1: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
<BUG-1>
{example_bug}
<FIXED-1>
{example_fix}
<BUG-2>
{example_bug_1}
<FIXED-2>
{example_fix_1}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res


def few_3(block: str, example_bug: str, example_fix: str, example_bug_1: str, example_fix_1: str, example_bug_2: str, example_fix_2: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
<BUG-1>
{example_bug}
<FIXED-1>
{example_fix}
<BUG-2>
{example_bug_1}
<FIXED-2>
{example_fix_1}
<BUG-3>
{example_bug_2}
<FIXED-3>
{example_fix_2}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res


def few_4(block: str, example_bug: str, example_fix: str, example_bug_1: str, example_fix_1: str,
                     example_bug_2: str, example_fix_2: str, example_bug_3: str, example_fix_3: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
<BUG-1>
{example_bug}
<FIXED-1>
{example_fix}
<BUG-2>
{example_bug_1}
<FIXED-2>
{example_fix_1}
<BUG-3>
{example_bug_2}
<FIXED-3>
{example_fix_2}
<BUG-4>
{example_bug_3}
<FIXED-4>
{example_fix_3}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res

def few_5(block: str, example_bug: str, example_fix: str, example_bug_1: str, example_fix_1: str,
                     example_bug_2: str, example_fix_2: str, example_bug_3: str, example_fix_3: str,
                     example_bug_4: str, example_fix_4: str) -> str:

    res = f"""Below is an example of a vulnerability code snippet fix.
The following is the vulnerable code snippet and the corresponding fixed code snippet:
```
<BUG-1>
{example_bug}
<FIXED-1>
{example_fix}
<BUG-2>
{example_bug_1}
<FIXED-2>
{example_fix_1}
<BUG-3>
{example_bug_2}
<FIXED-3>
{example_fix_2}
<BUG-4>
{example_bug_3}
<FIXED-4>
{example_fix_3}
<BUG-5>
{example_bug_4}
<FIXED-5>
{example_fix_4}
```

The current task is to fix the vulnerable code snippet below.
```
{block}
```

Your reply should only contain the fixed code snippet.
"""
    return res

