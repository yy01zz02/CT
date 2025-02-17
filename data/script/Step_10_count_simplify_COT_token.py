import json
import statistics


# 读取json文件
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 获取每个 "s_cot" 字段的单词数并计算统计数据
def process_data(data):
    word_counts = []

    for entry in data:
        if "s_cot" in entry:
            # 获取 "s_cot" 字段的字符串并按空格切割
            words = entry["s_cot"].split()
            # 将单词数追加到 word_counts 列表
            word_counts.append(len(words))

    return word_counts


# 计算统计信息
def calculate_statistics(word_counts):
    if not word_counts:
        return None  # 如果没有数据，返回None

    max_value = max(word_counts)
    min_value = min(word_counts)
    avg_value = sum(word_counts) / len(word_counts)
    median_value = statistics.median(word_counts)

    return max_value, min_value, avg_value, median_value


def func(file_path):
    # 设置文件路径


    # 读取数据
    data = read_json(file_path)

    # 处理数据，获取单词数列表
    word_counts = process_data(data)

    # 计算统计信息
    statistics_result = calculate_statistics(word_counts)

    if statistics_result:
        max_value, min_value, avg_value, median_value = statistics_result
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"Average: {avg_value}")
        print(f"Median: {median_value}")
    else:
        print("No data found.")


if __name__ == "__main__":
    file_path = "../SecCodePLT/SecCodePLT_final.json"  # 请替换成你的json文件路径
    func(file_path)
