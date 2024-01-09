import os
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from api.config import api_key_OPENAI

os.environ["OPENAI_API_KEY"] = api_key_OPENAI
model_id = 'gpt-3.5-turbo'

def get_stock_suggestion(query):
    loader = TextLoader("data.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 1}))
    print(qa.run(query))
