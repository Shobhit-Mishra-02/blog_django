from django.shortcuts import render, HttpResponse
from blog_tech.models import post

# Create your views here.
def home(request):
    all_posts = post.objects.all()
    req_posts = post.objects.extra(where=[f'id>{len(all_posts)-3}'])

    return render(request, 'home.html',{'content':req_posts})

def blog(request):
    req_post = post.objects.filter(status='main')
    return render(request, 'blog.html', {'content':req_post})

def about(request):
    return render(request, 'about.html')

def postview(request, id):
    req_post = post.objects.filter(id = id)
    links = post.objects.filter(tag = req_post[0].tag)
    return render(request, 'postview.html',{'content':req_post, 'links':links})

def search(request):
    if request.method == 'GET':
        search_name = request.GET.get('search')
        req_posts = post.objects.filter(title__icontains=f'{search_name}')

    return render(request, 'search.html',{'content':req_posts})