from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from avtoprokat.api.views import registration, GetUserCars, EditUserData, GetAllUsers

urlpatterns = [
    path('register', registration, name='register_'),
    path('login', obtain_auth_token, name='login_'),
    path('getusercars', GetUserCars.as_view(), name='get_cars'),
    path('edituser', EditUserData.as_view(), name='edit_user'),
    path('getallusers', GetAllUsers.as_view(), name='get_users'),
]