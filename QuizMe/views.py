from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Question,QuizSession
import random

def login_view(request):    
    if request.method=="POST":
        username,password=request.POST.get('username'),request.POST.get('password')
        if username=='admin' and password=='password':
            request.session['logged_in']=True
            return redirect('homepage')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout_view(request):
    del request.session['logged_in']
    return redirect('login')

def home_view(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request,'home.html')
def start_view(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    session=QuizSession.objects.create()
    question_ids=list(Question.objects.values_list('id',flat=True))
    random_question=random.sample(question_ids,min(5,len(question_ids)))
    request.session['random_question']=random_question
    return redirect('question',session_id=session.id,question_number=1)

def get_question(request,session_id,question_number):
    try:
        session=QuizSession.objects.get(id=session_id)
    except QuizSession.DoesNotExist:
        return redirect('login')
    random_question=request.session.get('random_question',[])
    question_id=random_question[-1]
    question=Question.objects.get(id=question_id)

    return render(request,'question.html',{'question':question,'session':session,'question_number':question_number})

def submit_answer(request,session_id,question_number):
    session=QuizSession.objects.get(id=session_id)
    random_question=request.session.get('random_question',[])
    qid=random_question[-1]
    question=Question.objects.get(id=qid)
    random_question.pop()
    request.session['random_question']=random_question
    answer=request.POST.get('answer')
    if answer==question.correct_choice:
        session.correct+=1
    else:
        session.incorrect+=1
    session.answered+=1
    session.save()
    if session.answered==5:
        return redirect('result',session_id=session.id)
    return redirect('question',session_id=session.id,question_number=question_number+1)

def result_view(request,session_id):
    session=QuizSession.objects.get(id=session_id)
    return render(request,'result.html',{'session':session})