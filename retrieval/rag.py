from retrieval.search import retriever
from ingestion.llm import llm, prompt
from langchain_core.runnables import RunnablePassthrough

rag_input = {
    "context": retriever,
    "question": RunnablePassthrough()
}

rag_chain = rag_input | prompt | llm

def ask_question(question):
    answer=rag_chain.invoke(question)
    return answer