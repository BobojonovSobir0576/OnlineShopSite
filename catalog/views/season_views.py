from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catalog.models import *
from catalog.forms import *


class SeasonCreateViews(CreateView):
    model = Seasson
    form_class = SeassonForm
    template_name = 'season/create.html'
    success_url = reverse_lazy('list_season')
    
@login_required
def season_list(request):
    context = {}
    context['obj_list'] = Seasson.objects.all()
    return render(request,'season/season_list.html/',context)

@login_required
def seaseonDelete(request,pk):
    obj_list = Seasson.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_season')

class SeasonDetailViews(DeleteView):
    model = Seasson
    template_name = 'season/season_detail.html'

class SeasonUpdateViews(UpdateView):
    model = Seasson
    form_class = SeassonForm
    template_name = 'season/create.html'
    success_url = reverse_lazy('list_season')
    
