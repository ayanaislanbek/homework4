from django.shortcuts import render
from .models import ClothesModel



def clothes_list(request):
    if request.method == "GET":
     clothes = ClothesModel.objects.all()
     return render(
        request,
        template_name='clothes/clothes.html'  ,
        context={
           'clothes': clothes,
           }
     )



def first_brand(request):
    if request.method == "GET":
        clothes = ClothesModel.objects.filter(brands_name__='Dolce&Gabbana')
        return render(
            request,
            'clothes/first_brand.html',
            context={'clothes': clothes}
        )

def second_brand(request):
    if request.method == "GET":
        clothes = ClothesModel.objects.filter(brands_name__='Alexander McQueen')
        return render(
            request,
            'clothes/second_brand.html',
            context={'clothes': clothes}
        )
   