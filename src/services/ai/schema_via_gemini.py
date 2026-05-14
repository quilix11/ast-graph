import os
from google import genai
from dotenv import load_dotenv

from src.services.ast_logic.parser import parser

load_dotenv()

def mermaid_schema():

    parser_data = parser()

    client = genai.Client(api_key=os.getenv("API_KEY"))

    response = client.models.generate_content(
        model=os.getenv("AI_MODEL"),
        contents=f"""
            Act as a Principal Software Architect. Create a high-end, professional Mermaid.js flowchart.

INPUT DATA:
{parser_data}

STRICT RULES:
1. OUTPUT ONLY THE RAW MERMAID CODE (No backticks, no comments outside the code).
2. Use 'graph TD'.
3. INCLUDE EXPLANATIONS:
    - Add descriptive labels to the arrows (e.g., "Sends AST data", "Requests Mermaid code").
    - Use Mermaid 'Notes' or 'Annotations' if possible, or just very clear edge labels.
4. GROUPS & STYLES:
    - Group by folders: "CORE", "SERVICES", "ENTRY".
    - Use professional colors: Main(#FFD700), Services(#F4F4F9).
5. CONTENT:
    - Describe the PURPOSE of each connection.
    - Example: main.py -- "Initializes process" --> ai_logic.py

Example format:
graph TD
    classDef main fill:#FFD700,stroke:#333;
    A("main.py"):::main -- "1. Starts the app" --> B("parser.py")
    B -- "2. Reads file content" --> C("reader.py")"""
    )

    return response.text


print(mermaid_schema())