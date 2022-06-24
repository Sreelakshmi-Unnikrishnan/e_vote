from urllib import response
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from winreg import QueryReflectionKey
from django.shortcuts import render, redirect

from .models import *
from .forms import *

# Create your views here.
def home(request):
    if request.method == 'GET':
        Q = Question.objects.all()
        c = {
        'Quests': Q,
        }
        return render(request, 'polls/home.html',c)

def votenow(request, pk):
        Q = Question.objects.get(id=pk)
        if 'Like' in request.POST:
            Q.likes = Q.likes + 1 
            Q.save()
        if 'DisLike' in request.POST:
            Q.dislikes = Q.dislikes + 1 
            Q.save()
        c = {
            'form': Q
        }
        return render(request,'polls/votenow.html',c)


def results(request, pk):  
    if request.method == 'GET':
        Q = Question.objects.get(id=pk) 
        c = {
            'form': Q
        }

    return render(request, 'polls/results.html', c)