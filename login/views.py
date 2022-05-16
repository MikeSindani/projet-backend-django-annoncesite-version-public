from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request,"login/signIn.html")
def signUp(request):
    return render(request,"login/signUp.html")
    