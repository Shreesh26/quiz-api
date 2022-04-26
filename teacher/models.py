from django.db import models
from userProcess.models import Teacher

class QuizName(models.Model):
    name=models.CharField(max_length=50)
    author=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    no_of_ques=models.IntegerField()
    def __str__(self):
        return self.name+" - "+ self.author.user.username

class QuizQuestion(models.Model):
    question=models.TextField()
    quiz=models.ForeignKey(QuizName, on_delete=models.CASCADE)
    marks=models.IntegerField()
    def __str__(self):
        return "question for "+self.quiz.name

class QuizOption(models.Model):
    option=models.TextField()
    question=models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    is_correct=models.BooleanField()
    def __str__ (self):
        return "option for "+self.question.quiz.name
