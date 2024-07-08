from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product, Category

# Create your views here.
def product(request):
    products = Product.objects.all()
    product_obj = Product.objects.get(id=2)
    categorys = Category.objects.get.all()
    context_name = {
        "product_list":products,
        "object":product_obj,
        "categorys":categorys,
        "name":"Darpan",
        "address":"Ktm",
        "phone":9880908909,



    }
    # print(products) #to print all list of product table objects
    # return JsonResponse({"message":"hello from product app"})
    return render(request, 'product_list.html', context=context_name) #UI MA DEKHOUNA RENDER

def create(request):
    if request.method=='POST':
        print(request.POST)
        pro_name = request.POST.get('name', '')
        # price=request.POST.get('price', '100O')
        price = request.POST.get('price', 1)
        added_by = request.user
        product_category = request.POST.get('product_category', 1)
        cat_obj = Category.objects.get(id=product_category)
        print(price)
        print(type(added_by), type(product_category))
        pro = Product.objects.create(name=pro_name, price=price, added_by=added_by, product_category_id=product_category)#fk case ma id
        #pro = Product.objects.create(name=pro_name, price=price, added_by_id=added_by, product_category=cat_obj)
    return render (request, 'product_list.html')
