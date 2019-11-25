"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from apps.mainsite.views import (home, index, callback, check, register)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('callback/', callback, name='callback'),
    path('check/', check, name='check'),
    path('register/', register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
