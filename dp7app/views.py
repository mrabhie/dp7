from django.shortcuts import render
from django.http import HttpResponse

def trial(request):
    return HttpResponse('<h1>Project is on air</h1>')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,"dp7app/home.html")

def profile(request):
    name="abhilash"
    return render(request,"dp7app/profile.html",{'name':name})
