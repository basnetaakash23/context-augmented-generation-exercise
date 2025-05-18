from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.services import ContextService
from chat.services.openai_service import OpenAIService
from chat.services.local_category_service import LocalCategoryService

class PromptAPIView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        prompt = request.data.get("prompt")

        context_service = ContextService(user_id)
        context_service.add_message("user", prompt)

        return Response({"message": "Prompt stored."}, status=status.HTTP_201_CREATED)

class ContextAPIView(APIView):
    def get(self, request, user_id):
        context_service = ContextService(user_id)
        context = context_service.get_context()
        return Response({"context": context}, status=status.HTTP_200_OK)

class ClearContextAPIView(APIView):
    def delete(self, request, user_id):
        context_service = ContextService(user_id)
        context_service.clear_context()
        return Response({"message": "Context cleared."}, status=status.HTTP_200_OK)
    
class ChatWithOpenAI(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        prompt = request.data.get("prompt")

        category_service = LocalCategoryService()
        category = category_service.classify(prompt)

        context_service = ContextService(user_id)
        context_service.add_message("user", prompt, category=category)

        filtered_context = context_service.get_context()
        filtered_context.append(("user", prompt))

        gpt = OpenAIService()
        reply = gpt.generate_reply(filtered_context, category)

        context_service.add_message("assistant", reply, category=category)

        return Response({
            "reply": reply,
            "category": category
            })
    
class CategorizePrompt(APIView):
    def get(self, request):
        user_id = request.data.get("user_id")
        prompt = request.data.get("prompt")

        category_service = LocalCategoryService()
        category = category_service.classify(prompt)
        return Response({"reply": category})


