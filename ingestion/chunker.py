from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120
)
chunks = text_splitter.split_documents(documents)