import json

import chromadb

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





