import os
import aiohttp
import json

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class InsightAgent:
    async def generate_insights(self, text: str) -> str:
        prompt = f"Analyze this document and provide 5-7 key insights:\n\n{text}"
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 800
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(GROQ_API_URL, json=payload, headers=headers, timeout=60) as resp:
                res = await resp.json()
                try:
                    return res["choices"][0]["message"]["content"]
                except Exception:
                    return "ERROR_INSIGHT: " + json.dumps(res)
