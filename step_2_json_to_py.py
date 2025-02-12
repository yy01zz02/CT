import json
import os

cnt = 0

def json_to_py(file_path, save_folder):
    global cnt

    # 尝试打开 JSON 文件，处理不同编码方式
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        # 如果 utf-8 读取失败，尝试使用 gbk 编码
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                data = json.load(f)
        except UnicodeDecodeError as e:
            print(f"无法读取文件 {file_path}，编码错误: {e}")
            return  # 如果文件仍然无法读取，跳过该文件

    # 创建保存 Python 文件的文件夹（如果不存在）
    os.makedirs(save_folder, exist_ok=True)

    # 遍历 JSON 数据并将每个 code 写入对应的 Python 文件
    for entry in data:
        try:
            cnt += 1
            file_name = f"{entry['ID']}.py"  # 文件名为 id.py
            file_path = os.path.join(save_folder, file_name)  # 文件保存路径

            # 获取代码并写入文件
            with open(file_path, 'w', encoding='utf-8') as py_file:
                py_file.write(entry['Fixed_code'])  # 将代码写入文件

        except KeyError as e:
            print(f"跳过条目，缺少必要的键：{e}")
            continue  # 如果缺少 'ID' 或 'Fixed_code' 键，跳过该条目

    print(f"所有 Python 文件已成功写入 {save_folder} 文件夹中")

# 设置文件路径和保存文件夹
file_path = 'data/SecCodePLT/fixed_and_reason_4.json'
save_folder = 'data/SecCodePLT/fixed_code_5'

json_to_py(file_path, save_folder)
print(f"共处理了 {cnt} 个文件。")
