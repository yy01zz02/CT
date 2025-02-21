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

# 添加到 Chroma 数据库
collection.add(
    embeddings=emb_fn(["The price of one?", "The price of two?", "The price of three?", "The price of four?",
                       "The price of five?"]),
    documents=["The price of one?", "The price of two?", "The price of three?", "The price of four?",
               "The price of five?"],
    metadatas=[{'data': "data one", 'number': "number one"}, {'data': "data two", 'number': "number two"},
               {'data': "data three", 'number': "number three"}, {'data': "data four", 'number': "number four"},
               {'data': "data five", 'number': "number five"}],
    ids=['1', '2', '3', '4', '5']  # 假设每个代码块有唯一的 id
)

new_code_block = "how much the double price?"

# 执行相似性搜索
results = collection.query(
    query_embeddings=emb_fn([new_code_block]),
    n_results=2  # 返回前 5 个最相似的结果
)

# 提取相似代码块的详细信息
for result in results['metadatas']:
    print(result)
    for res in result:
        print(res['data'], res['number'])
    # print(result['number'])
    # metadata = result['metadata']
    # print(f"Buggy Code: {metadata['buggy_code']}")
    # print(f"Fixed Code: {metadata['fixed_code']}")

print('----------------------------')

print(results['embeddings'])

print('----------------------------')
print(collection.peek())
