from Api_or_Url import GetApi
from Api_or_Url import GetUrl
from Api_or_Url import ConfigApi

from Chunking import Ids
from Chunking import LoadDocuments
from Chunking import Chunk

from Embendings import Embendder

from Generator import LLM

from Prompts import CreatePrompt

from Vectorstore import SetupQdran
from Vectorstore import VectorConnection

import os
import sys
sys.path.append(os.path.abspath("RAG/Config"))
import Config as cf



#Obtenmos las API Key
ApiGoogle = GetApi.GetApi.ApiGenai()
ApiQdrant = GetApi.GetApi.ApiQdrant()

#Obtenemos la Url de Qdrant
UrlQdrant = GetUrl.GetUrl.UrlQdrant()

#Fragmentamos los documentos
archivos = LoadDocuments.LoadAll()

#Creamos los chunks 
chunks = Chunk.GetChunk(archivos)

#Creamos una lista de ids para cada chunk
ids = Ids.CreateId(chunks)

#Creamos un cliente configurado de Genai
clienteGenai = ConfigApi.ConfigApi.ConfigGenai(ApiGoogle)

#Creamos un cliente configurado de Qdrant
clienteQdrant = ConfigApi.ConfigApi.ConfigQdrant(UrlQdrant,ApiQdrant)

#Creamos los embeddings
embeddings = Embendder.GetEmbedding(ApiGoogle)

#Cramos un collection name para Qdrant
collection_name = SetupQdran.Setup(clienteQdrant)

#Creamos una instancia de Qdrant
Qdrant = VectorConnection.CreateQdrant(clienteQdrant,collection_name,embeddings)

#Cargamos los chunks a nuestra vase de datos vectorizada
Qdrant.add_documents(documents = chunks, ids = ids)

#MOstar la consulta en pantalla
#Creamos una consulta

mem = []

while True:
    if(pregunta := input(">>>")) == "salir":break
    mem.append({
        "role":"user",
        "parts":pregunta
    })

    respuesta = CreatePrompt.Prompt(pregunta,mem,Qdrant,clienteGenai)


    print(respuesta)

    mem.append({
        "role":"model",
        "parts":respuesta
    })