from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import UpdateView,CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth .decorators import login_required
from catalog.models import *
from catalog.forms import *


class GuideUnitsMeasurementCreateViews(CreateView):
    model = GuideUnitsMeasurement
    form_class = GuideUnitsMeasurementForm
    template_name = 'guideUnitsMeasurement/create.html'
    success_url = reverse_lazy('list_guideUnitsMeasurement')
    
@login_required
def guideUnitsMeasurement_list(request):
    context = {}
    context['obj_list'] = GuideUnitsMeasurement.objects.all()
    return render(request,'guideUnitsMeasurement/guideUnitsMeasurement_list.html/',context)

@login_required
def guideUnitsMeasurementDelete(request,pk):
    obj_list = GuideUnitsMeasurement.objects.filter(pk=pk)[0]
    obj_list.delete()
    return redirect('list_guideUnitsMeasurement')

class GuideUnitsMeasurementDetailViews(DeleteView):
    model = GuideUnitsMeasurement
    template_name = 'guideUnitsMeasurement/guideUnitsMeasurement_detail.html'

class GuideUnitsMeasurementUpdateViews(UpdateView):
    model = GuideUnitsMeasurement
    form_class = GuideUnitsMeasurementForm
    template_name = 'guideUnitsMeasurement/create.html'
    success_url = reverse_lazy('list_guideUnitsMeasurement')
    
