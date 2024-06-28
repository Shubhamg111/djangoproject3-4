from django.urls import path
from . views import *

urlpatterns = [
    path('register/',userRegister),
    path('login/',userLogin),
    path('logout/',userlogout)
]
