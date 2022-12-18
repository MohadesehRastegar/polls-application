from django.shortcuts import render
from .models import Question,Choice

# Create your views here.

def index(request):
    questions=Question.objects.all()
    return render(request,'pollsapp/index.html',{'questions':questions})

def vote(request,pk):
    question=Question.objects.get(id=pk)
    options=question.choices.all()
    return render(request,'pollsapp/vote.html',{'question':question,'options':options})

def resualt(request):
    return render(request,'pollsapp/resualt.html',{})