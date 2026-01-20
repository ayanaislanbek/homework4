from django.shortcuts import render
from .models import ClothesModel
from django.views import generic



# class ClothesListView(generic.ListView):
#     model = ClothesModel
#     template_name = 'clothes/clothes.html'
#     context_object_name = 'clothes'


# class FirstBrandListView(generic.ListView):
#     model = ClothesModel
#     template_name = 'clothes/first_brand.html'
#     context_object_name = 'clothes'

#     def get_queryset(self):
#         return self.model.objects.filter(brands_name__namе='Dolce&Gabbana')


# class SecondBrandListView(generic.ListView):
#     model = ClothesModel
#     template_name = 'clothes/second_brand.html'
#     context_object_name = 'clothes'

#     def get_queryset(self):
#        return self.model.objects.filter(brands_name__name='Alexander McQueen')





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
        clothes = ClothesModel.objects.filter(brands_name__name='Dolce&Gabbana')
        return render(
            request,
            'clothes/first_brand.html',
            context={'clothes': clothes}
        )

def second_brand(request):
    if request.method == "GET":
        clothes = ClothesModel.objects.filter(brands_name__name='Alexander McQueen')
        return render(
            request,
            'clothes/second_brand.html',
            context={'clothes': clothes}
        )
   