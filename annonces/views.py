from django.shortcuts import render

# Create your views here.
def elevage(request):
    return render(request,"annonces/elevage.html")
def agriculture(request):
    return render(request,"annonces/agriculture.html")