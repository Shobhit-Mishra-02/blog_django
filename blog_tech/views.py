from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home page')

def blog(request):
    return HttpResponse('blog page')

def about(request):
    return HttpResponse('about page')