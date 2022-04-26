from django.urls import include, path
from . import views

urlpatterns = [
    path("reg_attempt/", views.StartQuiz().as_view(), name="quiz_reg"),
    path("ques/", views.AttemptQuestion().as_view(), name="ques_attempt"),
]