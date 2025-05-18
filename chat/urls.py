from django.urls import path
from .views import PromptAPIView, ContextAPIView, ClearContextAPIView, ChatWithOpenAI, CategorizePrompt

urlpatterns = [
    path("prompt/", PromptAPIView.as_view(), name="prompt"),
    path("context/<str:user_id>/", ContextAPIView.as_view()),
    path("context/<str:user_id>/clear/", ClearContextAPIView.as_view()),
    path("chat/", ChatWithOpenAI.as_view(), name="chat-openai"),
    path("categorize/", CategorizePrompt.as_view(), name="categorize")
]
