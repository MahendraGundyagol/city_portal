
from django.contrib import admin
from django.urls import path, include
from capp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('capp.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'), 
]
