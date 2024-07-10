from django.urls import path,include
from products.views import product, create, category_list, category_create



urlpatterns = [
  path("",product, name="product_list"), 
  path("category-create", category_create, name="cat_create"),
  path("create",create, name="product_create"),
  path("category-list", category_list, name="category_list")
    
]