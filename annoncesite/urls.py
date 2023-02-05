
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('login.urls')), 
    path('',include('contact.urls')),
    path('',include('annonces.urls')),
    path('',include('dashbord.urls')),
    path('',include('description.urls')),
    path('',include('searchApp.urls')),
    path('',include('space_member_app.urls')),  
    path('',include('download_app.urls')),  
    path('',include('mobile_app.urls')), 
]

# pour les page 404 et 500 
handler404 = 'error_page_app.views.error_404'
handler500 = 'error_page_app.views.error_500'


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)