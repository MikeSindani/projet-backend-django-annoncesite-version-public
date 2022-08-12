from distutils.log import error
from django.shortcuts import render

# Create your views here.


def error_404(request,exception):
        
        return render(request,'error/page_404.html')

def error_500(request):
        
        return render(request,'error/page_500.html')