from chromadb import Documents, EmbeddingFunction, Embeddings
from FlagEmbedding import BGEM3FlagModel


class MyEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        # 在初始化时创建模型实例
        self.model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)

    def __call__(self, texts: Documents) -> Embeddings:
        embeddings = self.model.encode(texts, max_length=1024)['dense_vecs']
        return embeddings


def main():
    emb_fn = MyEmbeddingFunction()
    val = emb_fn(["The price of one?", "The price of two?", "The price of three?", "The price of four?",
               "The price of five?"])
    print(type(val))
    print(val)
    print(len(val[0]))
    # 显式释放模型资源
    del emb_fn.model  # 删除模型引用，触发析构


if __name__ == "__main__":
    main()

