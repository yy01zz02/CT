import json


def format_fields(s_cot, bug, fixed_code):

    return {
        "instruction": (
            "Analyze the provided vulnerable code and generate a step-by-step chain-of-thought explanation to explain your reasoning, "
            "then provide the fixed code snippet. Your final answer should include both your reasoning and the corrected code."
        ),
        "input": (
            "Vulnerable Code:\n"
            f"{bug}"
        ),
        "output": (
            "Chain-of-Thought Explanation:\n"
            f"{s_cot.strip()}\n\n"
            "Fixed Code:\n"
            f"{fixed_code}"
        )
    }

# def format_fields(s_cot, bug, fixed_code):
#     return {
#         "instruction": (
#             "Based on the provided chain-of-thought explanation, correct the vulnerability in the code snippet. "
#             "The chain-of-thought outlines the step-by-step reasoning required to identify and fix the issue."
#         ),
#         "input": (
#             "Vulnerable Code Snippet:\n"
#             f"{bug}"
#             "Chain-of-Thought Explanation:\n"
#             f"{s_cot.strip()}"
#         ),
#         "output": fixed_code,
#     }


data_names = ['CyberSecEval', 'PromSec', 'SecCodePLT', 'SecurityEval']
vers = "2"

for data_name in data_names:

    output_file = f"{data_name}/{data_name}_SFT_CF.json"
    output_data = []

    for sub_data in data_names:
        if sub_data == data_name:
            continue

        input_file = f"{sub_data}/{sub_data}_{vers}.json"

        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)


        for record in data:
            s_cot = record.get("s_cot", "")
            bug = record.get("bug", "")
            fixed_code = record.get("fixed_code", "")

            # 调用格式化处理函数
            formatted_entry = format_fields(s_cot, bug, fixed_code)
            output_data.append(formatted_entry)

    print(len(output_data))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

