from openai import OpenAI
from django.conf import settings

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_reply(self, context, category):
        system_instruction = "You are a helpful assistant."
        if category:
            system_instruction += f"The user is asking about {category}. Provide information accordingly."

        
        messages = [{"role": role, "content": msg} for role, msg in context]
        print(messages)

        # Add system message if you want
        messages.insert(0, {
            "role": "system",
            "content": "You are a helpful assistant. Respond clearly and concisely."
        })

        response = self.client.chat.completions.create(model="gpt-4o-mini",
        messages=messages,
        max_tokens=300,
        temperature=0.7)

        return response.choices[0].message.content
