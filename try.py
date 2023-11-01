from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

documents = SimpleDirectoryReader('data').load_data()

path_to_key = r"C:\Users\User\Desktop\Учёба\опд\траю лламу"
key_name = 'api key.txt'
full_key_path = os.path.join(path_to_key, key_name)
api_key = open(full_key_path, 'r').readline()
os.environ['OPENAI_API_KEY'] = api_key

index = VectorStoreIndex.from_documents(documents)

# переводим индекс в режим поискового движка
query_engine = index.as_query_engine()

# запрос к базе знаний
response = query_engine.query(
    'о чем файлы?'
)
print(response.response)
