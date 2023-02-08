from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catalog.models import *



def create_models(request):
    context = {}
    context['brand'] = Brands.objects.all()
    if request.method == 'POST':
        brand = Brands.objects.get(id = request.POST['brands'])
        name = request.POST['name']
        if brand == "" or name == "":
            context['error'] = ""
            return render(request,'models/create.html',context)
        models_create = Models.objects.create(brand = brand, name=name)
    return render(request,'models/create.html',context)

def update_models(request,pk):
    context = {}
    context['brand'] = Brands.objects.all()
    context['models'] = Models.objects.filter(id=pk)[0]
    if request.method == 'POST':
        brand = Brands.objects.get(id = request.POST['brands'])
        name = request.POST['name']
        if brand == "" or name == "":
            context['error'] = ""
            return render(request,'models/create.html',context)
        context['models'].brand = brand
        context['models'].name = name
        context['models'].save()    
    return render(request,'models/update.html',context)

def list_models(request):
    context = {}
    context['all_model'] = Models.objects.all().order_by("-id")
    return render(request,'models/list_models.html',context)

def detail_models(request,pk):
    context = {}
    context['models'] = Models.objects.filter(id=pk)[0]   
    return render(request,'models/detail.html',context)

def delete_models(request,pk):
    context = {}
    context['models'] = Models.objects.filter(id=pk)[0]
    context['models'].delete()   
    return redirect('list_model')
    