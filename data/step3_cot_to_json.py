import json
import chromadb
from FlagEmbedding import BGEM3FlagModel
from chromadb import Documents, EmbeddingFunction, Embeddings

device = "cuda"

bge_model = BGEM3FlagModel('BAAI/bge-m3',
                           use_fp16=True)


class MyEmbeddingFunction(EmbeddingFunction):
    def __call__(self, texts: Documents) -> Embeddings:
        embeddings = bge_model.encode(texts, max_length=1024)['dense_vecs']
        return embeddings


emb_fn = MyEmbeddingFunction()

vers = "2"
data_names = ['SecurityEval', 'CyberSecEval', 'PromSec', 'SecCodePLT']
for name in data_names:

    # 漏洞数据集
    with open(f'{name}/{name}_{vers}.json', 'r', encoding='utf-8') as file_b:
        cur_data = json.load(file_b)

    client = chromadb.Client()
    collection = client.create_collection(
        name=name,
        embedding_function=emb_fn,
        metadata={
            "hnsw:space": "cosine",
        }
    )

    for sub_data in data_names:
        if sub_data == name:
            continue

        data_path = f'{sub_data}/{sub_data}_{vers}.json'

        with open(data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            # 每次插入之前，获取数据库当前的条目数

            cnt = collection.count()
            bug = item.get('bug')
            # bug_before = item.get('bug_before')
            # bug_after = item.get('bug_after')
            fixed_code = item.get('fixed_code')
            # cot = item.get('cot')
            s_cot = item.get('s_cot')

            # 添加到 Chroma 数据库
            collection.add(
                documents=[bug],
                metadatas=[
                    {'fixed_code': fixed_code, 's_cot': s_cot}],
                ids=[str(cnt + 1)]  # 使用当前的 ID
            )

    save_data = []
    ttt = 0
    for item in cur_data:
        id = item.get('id')
        bug = item.get('bug')
        print(bug)
        print('----------------------------')
        search_exp = collection.query(
            query_embeddings=emb_fn([bug]),
            n_results=2  # 返回前 n 个最相似的结果
        )

        # meta_data = search_exp['metadatas'][0][0]
        # exp_bug = search_exp['documents'][0][0]
        meta_data_0 = search_exp['metadatas'][0][0]
        exp_bug_0 = search_exp['documents'][0][0]

        meta_data_1 = search_exp['metadatas'][0][1]
        exp_bug_1 = search_exp['documents'][0][1]

        # meta_data_2 = search_exp['metadatas'][0][2]
        # exp_bug_2 = search_exp['documents'][0][2]

        # meta_data_3 = search_exp['metadatas'][0][3]
        # exp_bug_3 = search_exp['documents'][0][3]

        # meta_data_4 = search_exp['metadatas'][0][4]
        # exp_bug_4 = search_exp['documents'][0][4]


        # print(meta_data_0)
        # print()
        # print(exp_bug_0)
        # print('-------------------------------')
        #
        # print(meta_data_1)
        # print()
        # print(exp_bug_1)
        # print('-------------------------------')
        #
        # print(meta_data_2)
        # print()
        # print(exp_bug_2)
        # print('-------------------------------')

        #
        # exit(0)
        # print('----------------------------')
        ttt += 1
        print(ttt)
        json_path = f'{name}/{name}_cot_{vers}_few_2.json'

        save_data.append({**item, 'exp_bug_0': exp_bug_0, 'meta_data_0': meta_data_0,
                          'exp_bug_1': exp_bug_1, 'meta_data_1': meta_data_1})

        # 重新写回文件
        with open(json_path, 'w', encoding='utf-8') as file_j:
            json.dump(save_data, file_j, ensure_ascii=False, indent=4)
