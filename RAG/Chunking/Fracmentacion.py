from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_community.vectorstores import Qdrant
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter

from collections import deque


import os
import sys

sys.path.append(os.path.abspath("Config"))

import Config as cf

path = os.path.join(os.getcwd(), "Doc")

data = os.listdir(path)

archivos = list()

for archivo in data:
    pathArchivo = os.path.join(path,archivo)
    
    if str.endswith(pathArchivo, ".md") or str.endswith(pathArchivo, ".txt"):
        documentos = TextLoader(pathArchivo, encoding="utf-8").load()
    
    elif str.endswith(pathArchivo, ".pdf"):
        documentos = PyPDFLoader(pathArchivo).load()
    elif str.endswith(pathArchivo, ".cvs"):
        documentos = CSVLoader(pathArchivo, encoding="utf-8").load()
    else:
        continue

    archivos.extend(documentos)
#Se queda
Text_Spliter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 150,
)
#se queda
chunks =  Text_Spliter.split_documents(archivos)

load_dotenv()


api_key = os.getenv("Api_key_Google")

if api_key is None:
    print("❌ Clave no encontrada. Verifica el .env.")
else:
    print("✅ API key cargada correctamente.")

genai.configure(api_key=api_key)

client = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # o el modelo que desees
)

embending = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)

Base_datos = QdrantClient(
    url="https://7a5a73af-2cbc-4c57-97b2-93365711fb6d.eu-west-2-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.Hoc36m-OAzxEHMU0sn6IA0FqBUX2R3exvBx70XGqyr4"
)

ids = list()

for i, chunk in enumerate(chunks):
    ids.append(i)


collection_name = "embedding_data"
if not Base_datos.collection_exists(collection_name):
    Base_datos.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=1500,       
            distance=Distance.COSINE
        )
    )

qdrant = Qdrant(
    client=Base_datos,
    collection_name = collection_name,
     embeddings=embending
)

qdrant.add_documents(documents = chunks, ids = ids)

def Busqueda(consulta, k=5):
    s = ""
    fragmentos = qdrant.similarity_search(consulta, k)

    for fragmento in fragmentos:
        s += f"Fuente : {fragmento.metadata["source"]}\n"
        s += fragmento.page_content + "\n"

    return s
    
def Memoria(historial):
    cola = deque(maxlen=cf.MEMORIA)

    for usuario, bot in historial:
        cola.append({
            "role":"user",
            "parts": usuario
            })
        cola.append({
            "role":"model",
            "parts": bot
            })
        
    mensajes = list(cola)

    mensajes.insert(0, {
            "role": "user",
            "parts":cf.PROMPT_SISTEMA
        })

    return mensajes

def Consulta(pregunta, historial):
    mensaje = Memoria(historial)
    contexto = Busqueda(pregunta, k=cf.DOCUMENTOS)

    prompt = f"""
            Pregunta : {pregunta}
            Contexto : {contexto}
            Siempre responde en el idioma de la pregutna
    """

    mensaje.append({
            "role":"user",
            "parts": prompt
    })

    chat = client.start_chat(history=mensaje)

    respusta = chat.send_message(prompt)

    return respusta.candidates[0].content.parts[0].text

mem = []

while True:
    if(pregunta := input(">>>")) == "salir":break
    mem.append({
        "role":"user",
        "parts":pregunta
    })

    respuesta = Consulta(pregunta,mem)


    print(respuesta)

    mem.append({
        "role":"model",
        "parts":respuesta
    })


