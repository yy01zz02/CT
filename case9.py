import json


def count_flags(json_file):
    try:
        # 打开并读取json文件
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 初始化计数器
        count_flag_0 = 0
        count_flag_1 = 0
        total_count = len(data)

        # 遍历json数据，统计“flag”为"0"或"1"的数量
        for item in data:
            if item.get('flag') == '0':
                count_flag_0 += 1
            elif item.get('flag') == '1':
                count_flag_1 += 1

        # 输出统计结果
        print(f"文件总数量: {total_count}")
        print(f"flag: '0' 的数量: {count_flag_0}")
        print(f"flag: '1' 的数量: {count_flag_1}")

    except Exception as e:
        print(f"读取文件时发生错误: {e}")


# 调用函数，传入json文件路径
json_file_path = 'C:/Users/26979/Desktop/Qwen2.5-Coder-7B-Instruct/CyberSecEval/prompt_not_cot.json'  # 替换为你的json文件路径
count_flags(json_file_path)
print('--------------------------------')
json_file_path = 'C:/Users/26979/Desktop/Qwen2.5-Coder-7B-Instruct/CyberSecEval/prompt_cot.json'  # 替换为你的json文件路径
count_flags(json_file_path)
