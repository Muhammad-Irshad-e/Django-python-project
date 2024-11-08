from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')
def login_disp(request):
    return render(request,'login.html')
def news_disp(request):
    return render(request,'news.html')
def about_disp(request):
    return render(request,'about.html')
def contact_disp(request):
    return render(request,'contact.html')
def cycle_disp(request):
    return render(request,'cycle.html')
def register_disp(request):
    return render(request,'register.html')