from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catalog.models import *



def create_SetCharesteristicProduct(request):
    context = {}
    context['GuideCharacteristic'] = GuideCharacteristic.objects.all()
    context['GuideUnitsMeasurement'] = GuideUnitsMeasurement.objects.all()
    if request.method == 'POST':
        GuideCharacteristic = GuideCharacteristic.objects.get(id = request.POST['GuideCharacteristic'])
        GuideUnitsMeasurement = GuideUnitsMeasurement.objects.get(id = request.POST['GuideUnitsMeasurement'])
        value = request.POST['value']
        if GuideCharacteristic == "" or value == "" or GuideUnitsMeasurement == "":
            context['error'] = ""
            return render(request,'SetCharesteristicProduct/create.html',context)
        models_create = SetCharesteristicProduct.objects.create(GC = GuideCharacteristic,GUM=GuideUnitsMeasurement, value=value)
    return render(request,'SetCharesteristicProduct/create.html',context)

def update_SetCharesteristicProduct(request,pk):
    context = {}
    context['GuideCharacteristic'] = GuideCharacteristic.objects.all()
    context['GuideUnitsMeasurement'] = GuideUnitsMeasurement.objects.all()
    context['SetCharesteristicProduct'] = SetCharesteristicProduct.objects.filter(id=pk)[0]
    if request.method == 'POST':
        GuideCharacteristic = GuideCharacteristic.objects.get(id = request.POST['GuideCharacteristic'])
        GuideUnitsMeasurement = GuideUnitsMeasurement.objects.get(id = request.POST['GuideUnitsMeasurement'])
        value = request.POST['value']
        if GuideCharacteristic == "" or value == "" or GuideUnitsMeasurement == "":
            context['error'] = ""
            return render(request,'SetCharesteristicProduct/create.html',context)
        context['SetCharesteristicProduct'].GC = GuideCharacteristic
        context['SetCharesteristicProduct'].GUM = GuideUnitsMeasurement
        context['SetCharesteristicProduct'].value = value
        context['SetCharesteristicProduct'].save()    
    return render(request,'SetCharesteristicProduct/update.html',context)

def list_SetCharesteristicProduct(request):
    context = {}
    context['all_model'] = SetCharesteristicProduct.objects.all().order_by("-id")
    return render(request,'SetCharesteristicProduct/list_SetCharesteristicProduct.html',context)

def detail_SetCharesteristicProduct(request,pk):
    context = {}
    context['SetCharesteristicProduct'] = SetCharesteristicProduct.objects.filter(id=pk)[0]   
    return render(request,'SetCharesteristicProduct/detail.html',context)

def delete_SetCharesteristicProduct(request,pk):
    context = {}
    context['SetCharesteristicProduct'] = SetCharesteristicProduct.objects.filter(id=pk)[0]
    context['SetCharesteristicProduct'].delete()   
    return redirect('list_SetCharesteristicProduct')
    