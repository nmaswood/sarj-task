# app/utils/llm.py
import openai

openai.api_key = "your-openai-api-key"

async def analyze_with_llm(text: str, prompt: str):
    response = await openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{prompt}\n\nText: {text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
