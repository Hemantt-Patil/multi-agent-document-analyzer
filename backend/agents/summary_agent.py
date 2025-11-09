import os
import aiohttp
import json

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class SummaryAgent:
    async def summarize(self, text: str, insights: str) -> str:
        prompt = (
            "You are a senior analyst. Summarize the following document and insights "
            "into an executive summary:\n\n"
            f"DOCUMENT:\n{text}\n\nINSIGHTS:\n{insights}"
        )
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
                    return "ERROR_SUMMARY: " + json.dumps(res)
