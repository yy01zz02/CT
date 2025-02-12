import datasets
import json

# 加载数据集并允许执行远程代码
apr_dataset = datasets.load_dataset("NTU-NLP-sg/xCodeEval", "apr", trust_remote_code=True)

# 获取train数据集
train_data = apr_dataset['train']

# 筛选出 lang_cluster 为 'C' 的数据
filtered_data = train_data.filter(lambda x: x['lang_cluster'] == 'C')

# 将筛选出的数据转为字典列表
filtered_data_list = filtered_data.to_dict()

# 将数据保存到新的JSON文件
with open('filtered_data.json', 'w') as json_file:
    json.dump(filtered_data_list, json_file, indent=4)

print("Filtered data saved to 'filtered_data.json'")
