import os
import requests
import logging

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

logger = logging.getLogger(__name__)


def explain_error(error_text: str) -> str:
    """
    Sends error traceback to HuggingFace model
    and returns explanation text.
    """

    prompt = f"""
You are a senior Python ML engineer.
Explain the following error clearly and suggest a fix.

Error:
{error_text}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.3,
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        result = response.json()

        # HF returns list format
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]

        return str(result)

    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return "LLM explanation failed."
