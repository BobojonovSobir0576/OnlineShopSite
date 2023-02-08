from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from catalog.models import *
from catalog.forms import *


class CarTypesCreateViews(CreateView):
    model = CarTypes
    form_class = CarTypesForm
    template_name = 'season/create.html'
    success_url = reverse_lazy('list_season')
    
@login_required
def cartypes_list(request):
    context = {}
    context['obj_list'] = CarTypes.objects.all()
    return render(request,'cartypes/cartypes_list.html/',context)

@login_required
def cartypesDelete(request,pk):
    obj_list = CarTypes.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_cartypes')

class CarTypesDetailViews(DeleteView):
    model = CarTypes
    template_name = 'cartypes/cartypes_detail.html'

class CarTypesUpdateViews(UpdateView):
    model = CarTypes
    form_class = CarTypesForm
    template_name = 'cartypes/create.html'
    success_url = reverse_lazy('list_cartypes')
    
