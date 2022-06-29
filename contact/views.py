from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,"contact/contact.html")
def aboutus(request):
    return render(request,"aproposde/aproposde.html")