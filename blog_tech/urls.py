
from os import name
from django.urls import path
from blog_tech import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('postview/', views.postview, name='postview'),
    path('search/', views.search, name='search'),
]
