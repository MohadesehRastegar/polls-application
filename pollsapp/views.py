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

def result(request,pk ):
    question=Question.objects.get(id=pk)
    options=question.choices.all()


    if request.method=="POST":
        input_value=request.POST["choice"]
        selection_option=Choice.objects.get(id=input_value)
        
        selection_option.vote +=1
        selection_option.save()
        
        total_value=0
        for option in options:
            total_value+=option.vote
        
        percent_vote=100//total_value
        for option in options:
            option.percent=option.vote*percent_vote
            
            


        

        

    
    return render(request,'pollsapp/result.html',context={"question":question,"options":options})