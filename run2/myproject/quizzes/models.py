from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    questions = models.ManyToManyField('Question')

class Question(models.Model):
    text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)
