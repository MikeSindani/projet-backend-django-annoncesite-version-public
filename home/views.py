from django.http.response import HttpResponse
from django.shortcuts import render

context={'name':'hum'}
# Create your views here.
def home(request):
    return render(request,"home/home.html",context)

