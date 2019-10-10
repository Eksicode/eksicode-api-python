from django.urls import path, include
from .views import views as api_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [
    path('hello/', api_views.HelloView.as_view(), name="hello"),
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
    path('api/token/verify', verify_jwt_token, name='token_verify'),
]