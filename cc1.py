import json

def format_fields(s_cot, bug, fixed_code):

    return {
        "instruction": s_cot.strip(),
        "input": bug.strip(),
        "output": fixed_code.strip(),
    }

data_names = ['CyberSecEval', 'PromSec', 'SecCodePLT', 'SecurityEval']
vers = "2"

for data_name in data_names:

    output_file = f"{data_name}/{data_name}_SFT.json"
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
    # with open(output_file, "w", encoding="utf-8") as f:
    #     json.dump(output_data, f, ensure_ascii=False, indent=4)

