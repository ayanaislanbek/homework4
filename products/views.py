from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def product_one(request):
    if request.method == 'GET':
     return HttpResponse("Топ пять продуктов в Кореи: 1.Кимчи 2.Рамен 3.Кимпаб 4.Токпоки 5.Манду")
    
def product_two(request):
   if request.method == 'GET':
      time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
      return HttpResponse(f"дата и время: {time}")
   
def product_three(request):
   if request.method == 'GET':
      return  HttpResponse('<img src="https://www.modartt.com/images/ipacks/u4/u41-white.webp">' '<p>До Ре Ми Фа Соль Ля Си До</p>')
