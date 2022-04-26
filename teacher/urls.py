from django.urls import include, path
from . import views

urlpatterns = [
    path("add_test/", views.AddTest().as_view(), name="add_test"),
    path("add_ques/", views.AddQues().as_view(), name="add_ques"),
    path("add_option/", views.AddOption().as_view(), name="add_option"),
    path("performance/", views.ViewPerformance().as_view(), name="performance"),
]