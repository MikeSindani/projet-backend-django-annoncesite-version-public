from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request,"signIn/signIn.html")
def signUp(request):
    return render(request,"signUp/signUp.html")
    