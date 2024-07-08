from django.urls import path,include
from products.views import product, create

# urlpatterns = [
#   path("",product),
    
# ]

urlpatterns = [
  path("",product, name="product_list"), 
  path("create",create, name="product_create")
    
]