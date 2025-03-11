import json

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

client = chromadb.PersistentClient(path="D:/Chroma/CT1")

# client = chromadb.Client() # 只加载到内存

data_names = ["SecurityEval", "CyberSecEval", "PromSec", "SecCodePLT"]

for data_name in data_names:
    collection = client.create_collection(
        name=data_name,
        embedding_function=emb_fn,
        metadata={
            "hnsw:space": "cosine",
        }
    )


    for sub_data in data_names:
        if sub_data == data_name:
            continue

        data_path = f'{sub_data}/{sub_data}.json'

        with open(data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            # 每次插入之前，获取数据库当前的条目数

            cnt = collection.count()
            bug = item.get('bug')
            bug_before = item.get('bug_before')
            bug_after = item.get('bug_after')
            fixed_code = item.get('fixed_code')
            cot = item.get('cot')
            s_cot = item.get('s_cot')

            # 添加到 Chroma 数据库
            # collection.add(
            #     documents=[bug],
            #     metadatas=[{'bug_before': bug_before, 'bug_after': bug_after, 'fixed_code': fixed_code, 'cot': cot,
            #                 's_cot': s_cot}],
            #     ids=[str(cnt + 1)]  # 使用当前的 ID
            # )
            collection.add(
                documents=[bug],
                metadatas=[{'s_cot': s_cot}],
                ids=[str(cnt + 1)]  # 使用当前的 ID
            )
