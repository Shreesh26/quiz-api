from django.contrib.auth.models import User
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from teacher.models import QuizName, QuizOption, QuizQuestion, Teacher
from .models import *
from student.models import UserQuizSummary, UserQuizDetail
from django.contrib.auth.decorators import login_required

class AddTest(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def post(request):
        data=request.data
        name=data["name"]
        no_ques=data["no_ques"]
        user_upload=request.user
        author=Teacher.objects.filter(user=user_upload)[0]
        quiz=QuizName(name=name, author=author, no_of_ques=no_ques)
        quiz.save()
        return Response("Quiz added")

class AddQues(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def post(request):
        data=request.data
        quiz_id=data["quiz_id"]
        question=data["question"]
        marks=data["marks"]
        quiz=QuizName.objects.filter(pk=quiz_id)[0]
        ques=QuizQuestion(question=question, marks=marks, quiz=quiz)
        ques.save()
        return Response("Question Added Succesfully")

class AddOption(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def post(request):
        data=request.data
        ques_id=data["ques_id"]
        ques=QuizQuestion.objects.filter(pk=ques_id)[0]
        op_content=data["option"]
        is_correct=data["is_correct"]
        opt=QuizOption(option=op_content, question=ques, is_correct=is_correct)
        opt.save()
        return Response("Option Added Successfully")

class ViewPerformance(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def get(request):
        data=request.data
        quiz_id=data["quiz_id"]
        attempt_user=data["username"]
        quiz_object=QuizName.objects.filter(pk=quiz_id)[0]
        user=User.objects.filter(username=attempt_user)[0]
        attempt_query=UserQuizSummary.objects.filter(quiz_name=quiz_object, user=user)
        ques_attempted=UserQuizDetail.objects.filter(attempt=attempt_query[0])
        user_attempt=[{}]
        user_attempt[0]["summary"]=attempt_query.values()[0]
        user_attempt[0]["detail"]=ques_attempted.values()
        return Response(user_attempt)