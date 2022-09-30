from django.shortcuts import render

# Create your views here.

def download (resquest):
    return render(resquest, "download/download.html")
