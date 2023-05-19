"""
URL configuration for djangofication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='home' ),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('special/', views.special, name='special'),
    path('events/', views.event, name='event'),
    path('gallery/', views.gallery, name='gallery'),
    path('chefs/', views.chef, name='chef'),
    path('contact/', views.contact, name='contact'),
    path('Walter White/', views.chef1, name='walter'),
    path('Sarah Jhonson/', views.chef2, name='sarah'),
    path('William Anderson/', views.chef3, name='william'),

    
    
]
