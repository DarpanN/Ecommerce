from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def order(request):
    return JsonResponse({"message":"hello from orders app"})
