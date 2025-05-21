test_tool_result_content = """This notebook covers how to get started with the Chroma vector store. Chroma is a AI-native open-source vector database focused on developer productivity and happiness. Chroma is licensed under Apache 2.0. View the full docs of Chroma at this page, and find the API reference for the LangChain integration at this page.
To access Chroma vector stores you'll need to install the langchain-chroma integration package.

pip install -qU "langchain-chroma>=0.1.2"

Credentials
You can use the Chroma vector store without any credentials, simply installing the package above is enough!

If you want to get best in-class automated tracing of your model calls you can also set your LangSmith API key by uncommenting below:

# os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
# os.environ["LANGSMITH_TRACING"] = "true"


Initialization
Basic Initialization
Below is a basic initialization, including the use of a directory to save the data locally.

Select embeddings model:
pip install -qU langchain-openai

import getpass
import os

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)


Initialization from client
You can also initialize from a Chroma client, which is particularly useful if you want easier access to the underlying database.

import chromadb

persistent_client = chromadb.PersistentClient()
collection = persistent_client.get_or_create_collection("collection_name")
collection.add(ids=["1", "2", "3"], documents=["a", "b", "c"])

vector_store_from_client = Chroma(
    client=persistent_client,
    collection_name="collection_name",
    embedding_function=embeddings,
)

Manage vector store
Once you have created your vector store, we can interact with it by adding and deleting different items.

Add items to vector store
We can add items to our vector store by using the add_documents function.

from uuid import uuid4

from langchain_core.documents import Document

document_1 = Document(
    page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)

document_2 = Document(
    page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
    metadata={"source": "news"},
    id=2,
)

document_3 = Document(
    page_content="Building an exciting new project with LangChain - come check it out!",
    metadata={"source": "tweet"},
    id=3,
)

document_4 = Document(
    page_content="Robbers broke into the city bank and stole $1 million in cash.",
    metadata={"source": "news"},
    id=4,
)

document_5 = Document(
    page_content="Wow! That was an amazing movie. I can't wait to see it again.",
    metadata={"source": "tweet"},
    id=5,
)

document_6 = Document(
    page_content="Is the new iPhone worth the price? Read this review to find out.",
    metadata={"source": "website"},
    id=6,
)

document_7 = Document(
    page_content="The top 10 soccer players in the world right now.",
    metadata={"source": "website"},
    id=7,
)

document_8 = Document(
    page_content="LangGraph is the best framework for building stateful, agentic applications!",
    metadata={"source": "tweet"},
    id=8,
)

document_9 = Document(
    page_content="The stock market is down 500 points today due to fears of a recession.",
    metadata={"source": "news"},
    id=9,
)

document_10 = Document(
    page_content="I have a bad feeling I am going to get deleted :(",
    metadata={"source": "tweet"},
    id=10,
)

documents = [
    document_1,
    document_2,
    document_3,
    document_4,
    document_5,
    document_6,
    document_7,
    document_8,
    document_9,
    document_10,
]
uuids = [str(uuid4()) for _ in range(len(documents))]

vector_store.add_documents(documents=documents, ids=uuids)


API Reference:Document
['f22ed484-6db3-4b76-adb1-18a777426cd6',
 'e0d5bab4-6453-4511-9a37-023d9d288faa',
 '877d76b8-3580-4d9e-a13f-eed0fa3d134a',
 '26eaccab-81ce-4c0a-8e76-bf542647df18',
 'bcaa8239-7986-4050-bf40-e14fb7dab997',
 'cdc44b38-a83f-4e49-b249-7765b334e09d',
 'a7a35354-2687-4bc2-8242-3849a4d18d34',
 '8780caf1-d946-4f27-a707-67d037e9e1d8',
 'dec6af2a-7326-408f-893d-7d7d717dfda9',
 '3b18e210-bb59-47a0-8e17-c8e51176ea5e']

Update items in vector store
Now that we have added documents to our vector store, we can update existing documents by using the update_documents function.

updated_document_1 = Document(
    page_content="I had chocolate chip pancakes and fried eggs for breakfast this morning.",
    metadata={"source": "tweet"},
    id=1,
)

updated_document_2 = Document(
    page_content="The weather forecast for tomorrow is sunny and warm, with a high of 82 degrees.",
    metadata={"source": "news"},
    id=2,
)

vector_store.update_document(document_id=uuids[0], document=updated_document_1)
# You can also update multiple documents at once
vector_store.update_documents(
    ids=uuids[:2], documents=[updated_document_1, updated_document_2]
)


Delete items from vector store
We can also delete items from our vector store as follows:

vector_store.delete(ids=uuids[-1])

Query vector store
Once your vector store has been created and the relevant documents have been added you will most likely wish to query it during the running of your chain or agent.

Query directly
Similarity search
Performing a simple similarity search can be done as follows:

results = vector_store.similarity_search(
    "LangChain provides abstractions to make working with LLMs easy",
    k=2,
    filter={"source": "tweet"},
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

* Building an exciting new project with LangChain - come check it out! [{'source': 'tweet'}]
* LangGraph is the best framework for building stateful, agentic applications! [{'source': 'tweet'}]


Similarity search with score
If you want to execute a similarity search and receive the corresponding scores you can run:

results = vector_store.similarity_search_with_score(
    "Will it be hot tomorrow?", k=1, filter={"source": "news"}
)
for res, score in results:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")

* [SIM=1.726390] The stock market is down 500 points today due to fears of a recession. [{'source': 'news'}]


Search by vector
You can also search by vector:

results = vector_store.similarity_search_by_vector(
    embedding=embeddings.embed_query("I love green eggs and ham!"), k=1
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")

* I had chocalate chip pancakes and fried eggs for breakfast this morning. [{'source': 'tweet'}]


Other search methods
There are a variety of other search methods that are not covered in this notebook, such as MMR search or searching by vector. For a full list of the search abilities available for AstraDBVectorStore check out the API reference.

Query by turning into retriever
You can also transform the vector store into a retriever for easier usage in your chains. For more information on the different search types and kwargs you can pass, please visit the API reference here.

retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5}
)
retriever.invoke("Stealing from the bank is a crime", filter={"source": "news"})


[Document(metadata={'source': 'news'}, page_content='Robbers broke into the city bank and stole $1 million in cash.')]
""".strip()
