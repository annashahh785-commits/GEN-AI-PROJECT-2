from langchain_community.document_loaders import UnstructuredMarkdownLoader
loader = UnstructuredMarkdownLoader("C:\Users\Admin\Desktop\GEN AI PROJECT 2\documents\fashion_stylist_rag_documentation.md")
documents = loader.load()