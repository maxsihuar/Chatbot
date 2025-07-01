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


def CreateQdrant(Base_datos: QdrantClient, collection_name: str, embedding: Embeddings) -> Qdrant:
    """
    Crea una instancia del vector store Qdrant para gestionar búsquedas semánticas.

    Args:
        Base_datos (QdrantClient): Cliente conectado al servicio Qdrant.
        collection_name (string): Nombre de la colección en Qdrant.
        embedding (Embeddings): Objeto de embeddings para convertir textos a vectores.

    Returns:
        Qdrant: Instancia de vector store Qdrant lista para operaciones.
    """
    qdrant = Qdrant(
        client=Base_datos,
        collection_name = collection_name,
        embeddings=embedding
    )

    return qdrant
