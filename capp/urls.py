from django.contrib import admin
from django.urls import path,include
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('tourism/', views.tourism, name='tourism'),
    path('health/', views.health, name='health'),
    path('education/', views.education, name='education'),
    path('development/', views.development, name='development'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('water-power/', views.water_power_view, name='water_power'),
    path('water_power/', lambda request: redirect('water_power')),  # Redirect to correct URL
]

