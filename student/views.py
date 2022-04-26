from ast import Return
import imp
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from teacher.models import QuizName, QuizOption, QuizQuestion, Teacher
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required


class StartQuiz(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def post(request):
        data=request.data
        quiz_id=data["quiz_id"]
        quiz=QuizName.objects.filter(pk=quiz_id)
        quiz_date=date.today()
        user=request.user
        total_corr=0
        total_wrong=0
        max_marks=quiz.values()[0]['no_of_ques']*4
        percentage=((total_corr*4)/max_marks)*100
        quiz_detail=UserQuizSummary(quiz_name=quiz[0], quiz_date=quiz_date, user=user, total_corr=total_corr, total_wrong=total_wrong, scored_marks=total_corr*4, percentage=percentage, max_marks=max_marks)
        quiz_detail.save()
        return Response("User attempt added in database")

class AttemptQuestion(APIView):
    @staticmethod
    @login_required(login_url='/user/api/token/')
    def get(request):
        ques_id=request.data["ques_id"]
        ques=QuizQuestion.objects.filter(pk=ques_id)[0]
        ques_query=QuizQuestion.objects.filter(pk=ques_id).values()
        option=QuizOption.objects.filter(question=ques)
        quiz_ques={}
        quiz_ques['question']=ques_query[0]['question']
        option_dict={}
        for i in range(len(option.values())):
            option_dict[i+1]=option.values()[i]['option']

        quiz_ques['option']=option_dict
        return Response(quiz_ques)

    @staticmethod
    @login_required(login_url='/user/api/token/')
    def post(request):
        data=request.data
        ques_id=data["ques_id"]
        quiz_id=data["quiz_id"]
        answer_id=data['ans_id']
        attempt_id=data['attempt_id']
        quiz_query=QuizName.objects.filter(pk=quiz_id)[0]
        ques_query=QuizQuestion.objects.filter(pk=ques_id)
        ans_query=QuizOption.objects.filter(pk=answer_id).values()
        attempt_query=UserQuizSummary.objects.filter(pk=attempt_id).values()
        current_marks=attempt_query[0]["scored_marks"]
        max_marks=attempt_query[0]["max_marks"]
        total_corr=attempt_query[0]["total_corr"]
        total_wrong=attempt_query[0]["total_wrong"]
        if ans_query[0]["is_correct"]==True:
            current_marks=current_marks+4
            total_corr=total_corr+1
            user_ques_attempt=UserQuizDetail(attempt=UserQuizSummary.objects.filter(pk=attempt_id)[0], user=request.user, question=ques_query[0], option=QuizOption.objects.filter(pk=answer_id)[0], marks=4, quiz_name=quiz_query)
            user_ques_attempt.save()

        else:
            total_wrong=total_wrong+1
            user_ques_attempt=UserQuizDetail(attempt=UserQuizSummary.objects.filter(pk=attempt_id)[0], user=request.user, question=ques_query[0], option=QuizOption.objects.filter(pk=answer_id)[0], marks=0, quiz_name=quiz_query)
            user_ques_attempt.save()
        percentage=(current_marks/(max_marks))*100
        UserQuizSummary.objects.filter(pk=attempt_id).update(total_corr=total_corr, total_wrong=total_wrong, scored_marks=current_marks, percentage=percentage)
        return Response("Your response added successfully")
        
