from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from products.models import Products
from django.views import generic 



class SearchView(generic.ListView):
  template_name= 'products/products_list.html'
  context_object_name=  'products'
  model = Products

  def get_queryset(self):
     return self.model.objects.filter(name_models__icontains=self.request.GET.get("s"))
  
  def get_context_data(self, object_list=None, **kwargs):
     context =super().get_context_data(**kwargs)
     context['s'] = self.request.GET.get('s')
     return context




class ProductsView(generic.ListView):
    template_name = 'products/products_list.html'
    context_object_name =  'products'
    model = Products

    def get_queryset(self):
        return self.model.objects.all()




class ProductsDetailView(generic.DetailView):
    template_name = 'products/products_detail.html'
    model = Products
    context_object_name = 'product_id'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=product_id)
    



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
