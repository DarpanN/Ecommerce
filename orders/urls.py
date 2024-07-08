from django.urls import path,include
from orders.views import order

urlpatterns = [
  path("",order)  
    
]