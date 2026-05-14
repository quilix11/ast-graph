import base64
import zlib
from urllib.parse import urlencode
from pathlib import Path

import httpx

from src.services.ai.schema_via_gemini import mermaid_schema


def render():
    raw_text = mermaid_schema()
    text = raw_text.replace("```mermaid", "").replace("```", "").replace("<br>", "\n").strip() + "\n"
    print("--- GENERATED MERMAID SCHEMA ---")
    print(text)
    print("--------------------------------")
    import json
    state = {
        "code": text,
        "mermaid": "{\"theme\": \"neutral\"}",
        "autoSync": True,
        "updateDiagram": False
    }
    encoded = base64.urlsafe_b64encode(json.dumps(state).encode("utf-8")).decode("utf-8").rstrip("=")

    url = "https://mermaid.ink/img/" + encoded + "?" + urlencode({
        "type": "png", "width": "1000", "height": "1000"
    })

    content = httpx.get(url, timeout=60, follow_redirects=True).raise_for_status().content
    output_dir = Path("src/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "diagram.png").write_bytes(content)
