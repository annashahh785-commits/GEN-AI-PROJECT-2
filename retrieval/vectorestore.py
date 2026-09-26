from langchain_pinecone import PineconeVectorStore
from retrieval.embeddings import embeddings
vectorstore = PineconeVectorStore(
    index_name="fashion-qa",
    embedding=embeddings
)