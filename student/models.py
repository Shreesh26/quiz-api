from operator import mod
from tkinter import CASCADE
from turtle import onclick
from django.db import models
from teacher.models import QuizName, QuizOption, QuizQuestion
from django.contrib.auth.models import User

class UserQuizSummary(models.Model):
    quiz_name=models.ForeignKey(QuizName, on_delete= models.CASCADE)
    quiz_date=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total_corr=models.IntegerField(null=True, blank=True)
    total_wrong=models.IntegerField(null=True, blank=True)
    max_marks=models.IntegerField()
    scored_marks=models.IntegerField(default=0)
    percentage=models.FloatField()
    def __str__(self):
        return self.quiz_name.name+" - "+self.user.username

class UserQuizDetail(models.Model):
    attempt=models.ForeignKey(UserQuizSummary, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name=models.ForeignKey(QuizName, on_delete= models.CASCADE)
    question=models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    option=models.ForeignKey(QuizOption, on_delete=models.CASCADE)
    marks=models.IntegerField()
    def __str__(self):
        return "answer by "+self.user.username+" - "+self.question.question


