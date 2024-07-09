from langchain_astradb import AstraDBVectorStore    # Storing the data
# from langchain_openai import OpenAIEmbeddings       # Converting the data into embedding
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv                    # Loading the environment variable from the env file
import os
import pandas as pd
from ecommbot.data_converter import dataconveter     # Dataconverter takes the data 

load_dotenv()

# Required as secret variable can be kept in the .env file
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingestdata(status):
    vstore = AstraDBVectorStore(
            embedding=embedding,
            collection_name="chatbotecomm",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    # Check if the same data is nto passed the second time, if passed then it is skipped
    if storage==None:
        docs=dataconveter()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids

if __name__=='__main__':
    vstore,inserted_ids=ingestdata(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")
            

   