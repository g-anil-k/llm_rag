import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
# client = AsyncOpenAI()

class ChatService:

    def __init__(self):
        api_key=os.environ["OPEN_ROUTER_API_KEY"]

        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
            )

    async def ask(self, question: str):
        response = await self.client.chat.completions.create(
            model="xingchen-agi/xing4.0-29b-a4b:free",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return response.choices[0].message.content




async def main():
    chat_service = ChatService()
    query = input("Query:")
    response = await chat_service.ask(query)
    print("Response:", response)

if __name__ == "__main__":
    asyncio.run(main())