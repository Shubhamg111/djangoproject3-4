from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    
    path('allproducts/',allProducts),
    path('addcategory/',addCategory),
    path('addproducts/',addProduct),
    path('allcategory/',allCategory),
    path('deletecategory/<int:category_id>/',deleteCategory),
    path('updatecategory/<int:category_id>/',updateCategory),

    path('deleteproduct/<int:product_id>/',deleteProduct),
    path('updateproduct/<int:product_id>/',updateProduct)



    


   


]
