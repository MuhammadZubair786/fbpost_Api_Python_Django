from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'login.html')


def login_view(request):
    return render(request,'login.html')

def firebase_login(request):
    return render(request,"firebase_login.html")

def homepage(request):
    return render(request,"homepage.html")



