from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from catalog.models import *
from catalog.forms import *


class GuideCharacteristicCreateViews(CreateView):
    model = GuideCharacteristic
    form_class = GuideCharacteristicForm
    template_name = 'guideCharacteristic/create.html'
    success_url = reverse_lazy('list_guideCharacteristic')
    
@login_required
def guideCharacteristic_list(request):
    context = {}
    context['obj_list'] = GuideCharacteristic.objects.all()
    return render(request,'guideCharacteristic/guideCharacteristic_list.html/',context)

@login_required
def guideCharacteristicDelete(request,pk):
    obj_list = GuideCharacteristic.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_guideCharacteristic')

class GuideCharacteristicDetailViews(DeleteView):
    model = GuideCharacteristic
    template_name = 'guideCharacteristic/guideCharacteristic_detail.html'

class GuideCharacteristicUpdateViews(UpdateView):
    model = GuideCharacteristic
    form_class = GuideCharacteristicForm
    template_name = 'guideCharacteristic/create.html'
    success_url = reverse_lazy('list_guideCharacteristic')
    
