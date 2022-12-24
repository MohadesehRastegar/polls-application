from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')
    option=models.CharField(max_length=300)
    vote= models.IntegerField(default=0)
    percent=models.IntegerField(default=0)

    def __str__(self):
        return self.option