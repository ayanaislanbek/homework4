from django.shortcuts import render, get_object_or_404
from .models import Category, Product



def products_category(request, id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=id)
        products = products.objects.all() 
    return render(
        request,
        template_name='myShop/products.html',
        context={
            'category': category,
            'products': products
        }
    )



def categories_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
    return render(
        request,
        template_name='myShop/categories.html',
        context={
            'categories': categories
        }
    )


