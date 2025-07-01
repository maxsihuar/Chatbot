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

sys.path.append(os.path.abspath("Config"))

import Config as cf

import os
import sys



class LLM():
    @classmethod 
    def GenerateSearch(cls, consulta:str, qdrant:Qdrant, k:int=5) ->str | None:
        """
        Realiza una búsqueda semántica usando el motor de embeddings (Qdrant).

        Args:
            consulta (string): La consulta o pregunta del usuario.
            qdrant (Qdrant): El cliente Qdrant previamente configurado.
            k (int, opcional): Número de documentos similares a recuperar. Por defecto es 5.

        Returns:
            s (string): Texto concatenado de los fragmentos encontrados con su fuente.
        """
        s = ""
        fragmentos = qdrant.similarity_search(consulta, k)

        for fragmento in fragmentos:
            s += f"Fuente : {fragmento.metadata["source"]}\n"
            s += fragmento.page_content + "\n"

        return s
    @classmethod
    def GetMemory(cls, historial:list) -> list | None:
        """
        Construye la memoria conversacional previa para alimentar el modelo LLM.

        Args:
            historial (list()): Lista de tuplas [(usuario, respuesta_modelo), ...] representando el diálogo anterior.

        Returns:
            mensajes (list()): Lista de mensajes estructurados según el formato requerido por el modelo GenAI.
        """
        cola = deque(maxlen=cf.MEMORIA)

        for usuario, bot in historial:
            cola.append({
                "role": "user",
                "parts": usuario
            })
            cola.append({
                "role": "model",
                "parts": bot
            })
        
        mensajes = list(cola)

        mensajes.insert(0, {
            "role": "user",
            "parts": cf.PROMPT_SISTEMA
        })

        return mensajes

    