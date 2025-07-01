# 🧠 Consultas Medicas RAG Python

## Descripción

EvolvAI RAG Python es un sistema conversacional inteligente basado en la arquitectura **RAG (Retrieval-Augmented Generation)**, desarrollado en **Python**. Está diseñado para procesar documentos clínicos (PDF, CSV, TXT, MD), generar embeddings con **Google Gemini**, almacenarlos en **Qdrant** y responder preguntas utilizando contexto relevante y memoria conversacional.

---

## 🔧 Arquitectura

### Componentes principales

- **Chunking**: Fragmentación de documentos largos en trozos semánticos.
- **Embeddings**: Generación de vectores semánticos con Gemini (`embedding-001`).
- **Vectorstore**: Almacenamiento en Qdrant con recuperación semántica.
- **Prompts**: Estructura y formato de entrada para el modelo.
- **Generator**: Modelo LLM (Gemini) y lógica de conversación con memoria.
- **Config**: Variables de entorno, hiperparámetros y configuración global.
- **Main**: Orquestador principal del flujo RAG conversacional.

---

## 🔁 Flujo del sistema

1. Usuario hace una pregunta por consola.
2. Se busca contexto semántico en los documentos embebidos usando Qdrant.
3. Se forma un prompt contextualizado.
4. El modelo Gemini responde considerando:
    - Memoria conversacional previa (historial)
    - Prompt base y contexto de búsqueda
5. Se actualiza el historial para próximas respuestas.

---

## ⚙️ Tecnologías utilizadas

- **Python** 3.11+
- **Qdrant** (Cloud o local)
- **LangChain**
- **Google Generative AI** (Gemini)
- **.env** con claves API
- **Deque** para manejo de memoria temporal

---

## 📁 Estructura del Proyecto
    src/
    ├── Api_or_Url/
    │ ├── ConfigApi.py          # Configuración de URLs y claves
    │ ├── GetApi.py             # Obtención de la API Key
    │ └── GetUrl.py             # Obtención de la URL de Qdrant

    ├── Chunking/
    │ ├── Chunk.py              # Fragmentación lógica
    │ ├── Fracmentacion.py      # Script principal de procesamiento
    │ ├── Ids.py                # Generación de IDs para chunks
    │ └── LoadDocuments.py      # Carga de archivos (.pdf, .txt, .md, .csv)

    ├── Config/
    │ └── Config.py             # Variables globales como PROMPT, MEMORIA, etc.

    ├── Doc/
    │ └── *.pdf, *.md, etc.     # Documentos fuente a procesar

    ├── Embeddings/
    │ └── Embendder.py          # Encapsula generación de embeddings con Gemini

    ├── Generator/
    │ └── LLM.py                # Modelo de lenguaje y lógica de interacción

    ├── Prompts/
    │ └── CreatePrompt.py       # Estructuración del prompt

    ├── Vectorstore/
    │ ├── SetupQdran.py         # Creación de colección Qdrant
    │ └── VectorConnection.py   # Conexión con el cliente Qdrant

    ├── Main.py                 # Script principal para ejecutar todo
    ├── .env                    # API keys privadas
    ├── LICENSE
    └── README.md               # Este archivo


---

## 🚀 Ejecución

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/evolvai-rag-python.git
cd evolvai-rag-python

```
 ---

## 🗂️ Tipos de archivo soportados

Los siguientes tipos de archivo se procesan automáticamente desde la carpeta `/Doc`.  
Cada documento es fragmentado y embebido para permitir una búsqueda semántica eficiente.

### Tipos permitidos:

- `.pdf`
- `.txt`
- `.md`
- `.csv`

### 📍 Ubicación:

- Todos los archivos deben colocarse dentro de la carpeta: `/Doc`

### ⚙️ Proceso automático:

1. Detección del tipo de archivo.
2. Carga mediante los loaders correspondientes:
   - `TextLoader` para `.txt` y `.md`
   - `PyPDFLoader` para `.pdf`
   - `CSVLoader` para `.csv`
3. División en fragmentos (`chunking`).
4. Generación de vectores (`embeddings`).
5. Almacenamiento en la base de datos vectorial (Qdrant).

---

## 🌐 Interfaz Web

La carpeta `/Web` contiene una interfaz sencilla tipo chat en HTML+CSS+JS para interactuar con el modelo.

Puedes abrir `Web/index.html` directamente en tu navegador.

