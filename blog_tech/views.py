from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def postview(request):
    return render(request, 'postview.html')

def search(request):
    return render(request, 'search.html')