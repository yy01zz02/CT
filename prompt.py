code = ""
bandit_result = ""
reasoning_content = ""
example_bug_code = ""
example_cot = ""
example_fix_code = ""

# 获取推理模型生成的思维链，这个也可以直接用给测试小模型的prompt
reasoning_prompt = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable Code:
{code}

Bandit Analysis Results:
{bandit_result}

Please provide the fixed version of the code. Your response should only include the code, do not output anything else!!!
"""

# 简化推理模型生成的思维链
cot_prompt = f"""
I will provide a detailed reasoning process for the model to address the code vulnerability. 
Please generate a simplified and well-structured version of the Chain of Thought (COT). For example:
1. First, identify the main issue.
2. Next, break down the problem into smaller, manageable components.
3. Then, apply the most suitable method to resolve each component.
(There may be additional intermediate steps involved.)

Your response should only contain COT, no other content, and should be within 500 words!!!
Here is the original COT provided by the reasoning model:
{reasoning_content}
"""

# 给COT示例修复代码
cot_fix_prompt = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable code: 
{code}
 
Bandit analysis result: 
{bandit_result} 

Additionally, We have provided a similar bug fix example for reference:

Example Bug: 
{example_bug_code}

Example COT: 
{example_cot}

Example Fix: 
{example_fix_code}

Please apply this guidance to fix the vulnerability in the provided code. Your response should only contain code, do not output anything else!!!
"""

# 引导模型产生COT来修复
step_by_step_fix_prompt = f"""
You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.

Vulnerable code: 
{code}
 
Bandit analysis result: 
{bandit_result} 


Please take a thoughtful approach and fix the vulnerability step by step. Break down the process into clear, actionable steps, and explain your reasoning as you apply the solution. Finally, provide the corrected Python code.

"""
