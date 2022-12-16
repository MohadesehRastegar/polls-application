from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pollsapp/index.html',{})

def vote(request):
    return render(request,'pollsapp/vote.html',{})

def resualt(request):
    return render(request,'pollsapp/resualt.html',{})