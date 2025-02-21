import json

with open('experiment/dataset/CyberSecEval/CyberSecEval_Database.json', 'r', encoding='utf-8') as file:
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

client = chromadb.Client()
collection = client.create_collection(name='code', embedding_function=emb_fn)

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

new_code_block = '''
if __name__ == '__main__':
    import os,shelve
    import ppmatlab,numpy.oldnumeric as numpy
'''

# 执行相似性搜索
results = collection.query(
    query_embeddings=emb_fn([new_code_block]),
    n_results=2  # 返回前 5 个最相似的结果
)

# 提取相似代码块的详细信息
for result in results['documents']:
    for res in result:
        print(res)
        print('----------------------------')

for result in results['metadatas']:
    print(len(result))

    for res in result:
        print(res['buggy_code'])
        print(res['fixed_code'])
        print(res['reasoning_content'])
        print(res['s_cot'])

    # metadata = result['metadata']
    # print(f"Buggy Code: {metadata['buggy_code']}")
    # print(f"Fixed Code: {metadata['fixed_code']}")

print('----------------------------')

print(results['embeddings'])

print('----------------------------')
print(collection.peek())
