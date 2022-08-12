
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('login.urls')), 
    path('',include('contact.urls')),
    path('',include('annonces.urls')),
    path('',include('dashbord.urls')),
    path('',include('description.urls')),
    path('',include('searchApp.urls')),
    
]


handler404 = 'error_page_app.views.error_404'
handler500 = 'error_page_app.views.error_500'
