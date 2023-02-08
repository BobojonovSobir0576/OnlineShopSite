from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from catalog.models import *
from catalog.forms import *


class BrandsCreateViews(CreateView):
    model = Brands
    form_class = BrandsForm
    template_name = 'brand/create.html'
    success_url = reverse_lazy('list_brands')
    
@login_required
def brands_list(request):
    context = {}
    context['obj_list'] = Brands.objects.all()
    return render(request,'brands/brands_list.html/',context)

@login_required
def brandsDelete(request,pk):
    obj_list = Brands.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_brands')

class BrandsDetailViews(DeleteView):
    model = Brands
    template_name = 'brands/brands_detail.html'

class BrandsUpdateViews(UpdateView):
    model = Brands
    form_class = BrandsForm
    template_name = 'brands/create.html'
    success_url = reverse_lazy('list_brands')
    
