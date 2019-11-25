from django.urls import path
from .views import (
            callback,
            index,
            home,
            register,
            check
                    )
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',  home, name='home'),
    path('index/', index, name='index'),
    path('callback/', callback, name='callback'),
    path('check/', check, name='check'),
    path('register/', register, name="register")
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout')
]