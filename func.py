# logic.py

import requests

API_KEY = "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"
MODEL = "deepseek/deepseek-chat"

def get_reply(message):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers, timeout=20)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return "Error: " + str(e)
