from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from animes.views import profile_view
from animes.views import profile_view



urlpatterns = [
    path('', include('animes.urls')),         
    path('', include('usuarios.urls')), 
    path('profile/', profile_view, name='profile'),
    path('accounts/login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)