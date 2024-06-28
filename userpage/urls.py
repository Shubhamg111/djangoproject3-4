from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage),
    path('showallproducts',showallproducts),
    path('productview/<int:prod_id>',productView),

]
