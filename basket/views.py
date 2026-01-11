from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForm
from basket.models import Basket



def create_basket_view(request):
    if request.method == "POST":
     form = BasketForm(request.POST, request.FILES)
     if form.is_valid():
      form.save()
     return redirect('/basket_list/')
    else:
       form = BasketForm()

    return render (
       request,
       template_name='basket/create_basket.html',
       context={"form" : form}

    )




def show_basket_view(request):
  if request.method == "GET":
     basket = Basket.objects.all()
     return render(request, 
                   template_name='basket/basket_list.html',
                   context={'basket': basket}
                      )




def edit_user_view(request):
  basket_item = get_object_or_404(Basket, id)
  if request.method == "POST":
    form = BasketForm(request.POST, instance=basket_item)
    if form.is_valid():
      form.save()
      return  redirect ('/basket_list/')
    else:
      form = BasketForm(instance=basket_item)

    return render(request,
                template_name='basket/edit_basket.html',
              context= {'form': form}  
        )
  



def delete_basket_view(request,id):
    item = get_object_or_404(Basket, id=id)
    item.delete()
    return redirect('/basket_list/')