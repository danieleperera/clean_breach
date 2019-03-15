from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<H1>Ciao io sono la pagina home blog</H1>')
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/blog.html')