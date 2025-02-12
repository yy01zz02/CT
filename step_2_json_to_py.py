import json
import os

cnt = 0
def json_to_py(file_path, save_folder):
    # 读取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建保存 Python 文件的文件夹（如果不存在）
    output_folder = save_folder
    os.makedirs(output_folder, exist_ok=True)
    global cnt
    # 遍历 JSON 数据并将每个 code 写入对应的 Python 文件
    for entry in data:
        cnt += 1
        file_name = f"{entry['ID']}"  # 文件名为 id.py
        file_path = os.path.join(output_folder, file_name)  # 文件保存路径

        with open(file_path, 'w', encoding='utf-8') as py_file:
            py_file.write(entry['Fixed_code'])  # 将代码写入文件

    print(f"所有 Python 文件已成功写入 {output_folder} 文件夹中")


file_path = 'data/SecCodePLT/fixed_and_reason_1.json'
save_folder = 'data/SecCodePLT/fixed_code_2'


json_to_py(file_path, save_folder)
print(cnt)
