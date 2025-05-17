from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ContextService

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

