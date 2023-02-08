from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from catalog.models import *
from catalog.forms import *


class CountryManufacterCreateViews(CreateView):
    model = CountryManufacter
    form_class = CountryManufacterForm
    template_name = 'season/create.html'
    success_url = reverse_lazy('list_countryManufacter')
    
@login_required
def countryManufacter_list(request):
    context = {}
    context['obj_list'] = CountryManufacter.objects.all()
    return render(request,'countryManufacter/countryManufacter_list.html/',context)

@login_required
def countryManufacterDelete(request,pk):
    obj_list = CountryManufacter.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_countryManufacter')

class CountryManufacterDetailViews(DeleteView):
    model = CountryManufacter
    template_name = 'countryManufacter/countryManufacter_detail.html'

class CountryManufacterUpdateViews(UpdateView):
    model = CountryManufacter
    form_class = CountryManufacterForm
    template_name = 'countryManufacter/create.html'
    success_url = reverse_lazy('list_countryManufacter')
    
