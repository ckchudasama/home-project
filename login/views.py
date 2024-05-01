from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context={'page':'index'}
    return render(request,"index.html",context)

def success_page(request):
    return HttpResponse("<h1>hey this is a success page. </h1>")


def about(request):
    context={'page':'about'}
    return render(request,"about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request,"contact.html",context)
