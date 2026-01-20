from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views import generic


class ProductCategoriesListView(generic.ListView):
    template_name = 'myShop/categories.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.all()



class CategoriesListView(generic.ListView):
    template_name = 'myShop/categories.html'
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.all()
    

# def products_category(request, id):
#     if request.method == "GET":
#         category = get_object_or_404(Category, id=id)
#         products = products.objects.all() 
#     return render(
#         request,
#         template_name='myShop/products.html',
#         context={
#             'category': category,
#             'products': products
#         }
#     )


