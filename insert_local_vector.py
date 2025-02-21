import json

with open('experiment/dataset/SecurityEval/SecurityEval_Database.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3',
                       use_fp16=True)


class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        embeddings = model.encode(texts, max_length=1024)['dense_vecs']
        return embeddings


emb_fn = MyEmbeddingFunction()

client = chromadb.PersistentClient(path="D:/Chroma/CT")

# client = chromadb.Client() # 只加载到内存

collection = client.create_collection(name='SecurityEval', embedding_function=emb_fn)

for item in data:
    # 每次插入之前，获取数据库当前的条目数
    cnt = collection.count()

    block_code = item.get('block')
    buggy_code = item.get('buggy_code')
    fixed_code = item.get('fixed_code')
    reasoning_content = item.get('reasoning_content')
    s_cot = item.get('s_cot')

    # 添加到 Chroma 数据库
    collection.add(
        documents=[block_code],
        metadatas=[{'buggy_code': buggy_code, 'fixed_code': fixed_code, 'reasoning_content': reasoning_content,
                    's_cot': s_cot}],
        ids=[str(cnt + 1)]  # 使用当前的 ID
    )




