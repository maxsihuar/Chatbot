from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_community.vectorstores import Qdrant
import google.generativeai as Genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter

from collections import deque

import os
import sys

sys.path.append(os.path.abspath("Config"))

import Service.Config as cf
from Service.Generator.LLM import LLM


import re

def markdown_to_html(text: str) -> str:
    """
    Convierte Markdown básico a HTML: listas con '*', negritas con '**', y saltos de línea.
    """
    # Negrita **texto**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Listas: líneas que empiezan con '* '
    lines = text.splitlines()
    html_lines = []
    inside_ul = False

    for line in lines:
        if re.match(r'^\* ', line.strip()):
            if not inside_ul:
                html_lines.append('<ul>')
                inside_ul = True
            item = line.strip()[2:]
            html_lines.append(f'<li>{item}</li>')
        else:
            if inside_ul:
                html_lines.append('</ul>')
                inside_ul = False
            html_lines.append(line)

    if inside_ul:
        html_lines.append('</ul>')

    return '<br>'.join(html_lines)

def Prompt(pregunta:str, historial:list,client:Qdrant, Genai) -> str | None:
    """
        Genera una respuesta basada en la arquitectura RAG (Retrieval-Augmented Generation).

        Args:
                pregunta (str): Pregunta o consulta del usuario.
                historial (list): Lista de interacciones anteriores en formato [(usuario, respuesta_modelo), ...].
                client (GenerativeModel): Cliente GenAI configurado para manejar la conversación.

        Returns:
                str: Respuesta generada por el modelo, con contexto relevante incluido.
    """
    mensaje = LLM.GetMemory(historial)
    contexto = LLM.GenerateSearch(pregunta,client, k=cf.DOCUMENTOS)

    prompt = f"""
            Pregunta : {pregunta}
            Contexto : {contexto}
            Siempre responde en el idioma de la pregutna
    """

    mensaje.append({
            "role":"user",
            "parts": prompt
    })

    chat = Genai.start_chat(history=mensaje)

    respusta = chat.send_message(prompt)

    texto = respusta.candidates[0].content.parts[0].text.replace('\n', '<br>')

    respuesta_html = markdown_to_html(texto)

    return respuesta_html