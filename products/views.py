from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product, Category
from django.shortcuts import redirect
from django.urls import reverse
from products.forms import CategoryForm

# Create your views here.
def product(request):
    products = Product.objects.all()
    name = request.GET.get('name', False)
    # price = request.GET.get('price', False)

    cate = request.GET.get('name', False)

    print(name) #if kehe pathako xena vane false asyounxa nabai value
    if name:
        # products = Product.objects.filter(name=name)
        products = Product.objects.filter(name__icontains=name) #contains case sensivity hunxa icontains hudaina
    # if price:
        # products = Product.objects.filter(price=price)

    if cate:
        products = Product.objects.filter(product_category_id=cate)

    print(products)
    product_obj = Product.objects.get(id=2)
    categories = Category.objects.all()
    # print(categories)
    context_name = {
        "product_list":products,
        "object":product_obj,
        "categories":categories,
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
        # print(price)
        # print(type(added_by), type(product_category))
        pro = Product.objects.create(name=pro_name, price=price, added_by=added_by, product_category_id=product_category)#fk case ma id
        #pro = Product.objects.create(name=pro_name, price=price, added_by_id=added_by, product_category=cat_obj)

    return redirect (reverse("category_list"))
    return render (request, 'product_list.html')

def category_list(request) :
    # return JsonResponse ({"message":"data added from new redirect category_list urls"})
   return render (request, 'category_list.html')

def category_create(request):
    cat_form = CategoryForm()
    if request.method == "POST":
        data = request.POST
        # print(data)
        form = CategoryForm(data=data) 
        #to check valid form 
        if form.is_valid():
            form.save()
            return redirect(reverse("category_list"))#if data saved redirect to category list
        else:
           
           return render (request, 'category_create.html', {"form":form, "error": form.errors })
    
     
    return render (request, 'category_create.html', {"form":cat_form})

