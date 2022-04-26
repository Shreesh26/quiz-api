from django.contrib import admin

from .models import QuizName, QuizOption, QuizQuestion, Teacher
from.models import *

admin.site.register(Teacher)
admin.site.register(QuizName)
admin.site.register(QuizQuestion)
admin.site.register(QuizOption)
