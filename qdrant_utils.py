from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
from config import QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME


client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)


def create_collection_if_not_exists(vector_size: int):
if COLLECTION_NAME not in client.get_collections().collections:
client.recreate_collection(
collection_name=COLLECTION_NAME,
vectors_config=VectorParams(size=vector_size, distance="Cosine")
)




def insert_document(doc_id: int, vector, text: str):
client.upsert(
collection_name=COLLECTION_NAME,
points=[
PointStruct(id=doc_id, vector=vector, payload={"text": text})
]
)




def semantic_search(query_vector, limit=5):
results = client.search(
collection_name=COLLECTION_NAME,
query_vector=query_vector,
limit=limit
)
return results
