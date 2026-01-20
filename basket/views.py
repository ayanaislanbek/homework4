from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForm
from basket.models import Basket
from django.views import generic



class CreateBasketView(generic.CreateView):
  template_name='basket/create_basket.html'
  form_class = BasketForm
  success_url='/basket_list/'


  def form_valid(self, form):
    print(form.cleaned_data)
    return super(CreateBasketView, self).form_valid(form=form)
  



class ShowBasketView(generic.ListView):
  template_name = 'basket/basket_list.html'
  
  def get_queryset(self):
     return Basket.objects.all().order_by('-id')
  



class EditUserView(generic.UpdateView):
   template_name = 'basket/edit_basket.html'
   form_class = BasketForm
   success_url = '/basket_list/'

   def form_valid(self, form):
    print(form.cleaned_data)
    return super(EditUserView, self).form_valid(form=form)
   
   def get_object(self, **kwargs):
       item_id = self.kwargs.get('id')
       return get_object_or_404(Basket, id=item_id)

  

class DeleteBasketView(generic.DeleteView):
  template_name = 'basket/confirm_delete.html'
  success_url = '/basket_list/'
  def get_object(self, **kwargs):
    item_id = self.kwargs.get('id')
    return get_object_or_404(Basket, id=item_id)

