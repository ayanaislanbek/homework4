from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from products.models import Products


def products(request):
   if request.method == "GET":
      products = Products.objects.all()
      return render (
         request,
         template_name='products/products_list.html',
         context={
            'products': products
         }
      )
   


def product_detail(request,id):
   if request.method == "GET":
      products_id = get_object_or_404(Products, id=id)
   return render(
      request,
      template_name='products/products_detail.html',
      context={
         'products_id' : products_id
      }

   )



def korean_food(request):
    if request.method == 'GET':
     return HttpResponse("Топ пять продуктов в Кореи: 1.Кимчи 2.Рамен 3.Кимпаб 4.Токпоки 5.Манду")
    
def current_time(request):
   if request.method == 'GET':
      time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
      return HttpResponse(f"дата и время: {time}")
   
def about_me(request):
   if request.method == 'GET':
      return  HttpResponse('<img src="https://www.modartt.com/images/ipacks/u4/u41-white.webp">' '<p>До Ре Ми Фа Соль Ля Си До</p>')
