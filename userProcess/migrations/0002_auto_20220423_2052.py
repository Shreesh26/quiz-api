# Generated by Django 3.2.7 on 2022-04-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProcess', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizname',
            name='no_of_ques',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='marks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]