import json

import chromadb
from FlagEmbedding import BGEM3FlagModel

client = chromadb.PersistentClient(path="D:/Chroma/CT")
collection = client.get_collection("CyberSecEval")

print(collection.count())
with open('experiment/dataset/CyberSecEval/CyberSecEval_Database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(len(data))
print('----------------------------')

client = chromadb.PersistentClient(path="D:/Chroma/CT")
collection = client.get_collection("PromSec")

print(collection.count())
with open('experiment/dataset/PromSec/PromSec_Database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(len(data))
print('----------------------------')

client = chromadb.PersistentClient(path="D:/Chroma/CT")
collection = client.get_collection("SecCodePLT")

print(collection.count())
with open('experiment/dataset/SecCodePLT/SecCodePLT_Database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(len(data))
print('----------------------------')

client = chromadb.PersistentClient(path="D:/Chroma/CT")
collection = client.get_collection("SecurityEval")

print(collection.count())
with open('experiment/dataset/SecurityEval/SecurityEval_Database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(len(data))
print('----------------------------')


device = "cuda"
model_list = ["D:/DataSet/Qwen2.5-Coder-0.5B-Instruct/", "D:/DataSet/Qwen2.5-Coder-1.5B-Instruct/"]

bge_model = BGEM3FlagModel('BAAI/bge-m3',
                           use_fp16=True)

search_bug = 'You are a code vulnerability expert. Below is a vulnerable code snippet along with the results from Bandit security analysis. Your task is to fix the vulnerabilities and provide the corrected version of the code.'
emb_fn = MyEmbeddingFunction()

search_exp = collection.query(
                query_embeddings=emb_fn([search_bug]),
                n_results=1  # 返回前 1 个最相似的结果
            )

meta_data = search_exp['metadatas'][0]
fixed_code = meta_data['fixed_code']
buggy_code = meta_data['buggy_code']
cot = meta_data['reasoning_content']
s_cot = meta_data['s_cot']





