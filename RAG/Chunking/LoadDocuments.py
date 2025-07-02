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

def LoadAll() -> list | None:
    """
    Crea una lista de documentos los cuales se abstraen de la carpeta Doc
    Lee archivos con extensiones .md, .txt, .pdf y .csv, y los convierte en objetos
    Document compatibles con LangChain para procesamiento posterior.

    Args:
        None
    
    Returns:
        archivos(list()): Retorna una lista de archivos Laingchain
    """
    path = os.path.join(os.getcwd(), "RAG/Doc")

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

    return archivos