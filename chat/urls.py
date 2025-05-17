from django.urls import path
from .views import PromptAPIView, ContextAPIView, ClearContextAPIView

urlpatterns = [
    path("prompt/", PromptAPIView.as_view(), name="prompt"),
    path("context/<str:user_id>/", ContextAPIView.as_view()),
    path("context/<str:user_id>/clear/", ClearContextAPIView.as_view()),
]
