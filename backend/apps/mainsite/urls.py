from django.urls import path
from .views import (
            callback,
            index,
            home,
            register,
            check
                    )
urlpatterns = [
    path('',  home, name='home'),
    path('index/', index, name='index'),
    path('callback/', callback, name='callback'),
    path('check/', check, name='check'),
    path('register/', register, name="register")
]