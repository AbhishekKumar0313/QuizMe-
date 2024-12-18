from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    first_choice=models.CharField(max_length=200)
    second_choice=models.CharField(max_length=200)
    third_choice=models.CharField(max_length=200)
    fourth_choice=models.CharField(max_length=200)
    correct_choice=models.CharField(max_length=200,choices=[('1','1'),('2','2'),('3','3'),('4','4')])
    
    def __str__(self):
        return self.question_text
    
class QuizSession(models.Model):
    answered=models.IntegerField(default=0)
    correct=models.IntegerField(default=0)
    incorrect=models.IntegerField(default=0)
    
    def __str__(self):
        return f"Answered : {self.answered},Correct :  {self.correct},Incorrect : {self.incorrect}"
    
