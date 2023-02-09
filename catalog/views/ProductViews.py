from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from catalog.models import *
import os



def create_product(request):
    context = {}
    context['model'] = Models.objects.all()
    context['seasson'] = Seasson.objects.all()
    context['car_types'] = CarTypes.objects.all()
    context['SCP'] = SetCharesteristicProduct.objects.all()
    context['country_manu'] = CountryManufacter.objects.all()
    
    if request.method == 'POST':
        model = Models.objects.get(id = request.POST['model'])
        seasson = Seasson.objects.get(id = request.POST['seasson'])
        car_types = CarTypes.objects.get(id = request.POST['car_types'])
        SCP = SetCharesteristicProduct.objects.get(id = request.POST['SCP'])
        country_manu = CountryManufacter.objects.get(id = request.POST['country_manu'])
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['name']
        models_create = Product.objects.create(name = name,price=price,description = description, model=model,seasson = seasson,car_types = car_types, SCP=SCP,country_manu = country_manu, image=image)
    return render(request,'product/create.html',context)

def update_product(request,pk):
    context = {}
    context['model'] = Models.objects.all()
    context['seasson'] = Seasson.objects.all()
    context['car_types'] = CarTypes.objects.all()
    context['SCP'] = SetCharesteristicProduct.objects.all()
    context['country_manu'] = CountryManufacter.objects.all()
    context['product'] = Product.objects.filter(id=pk)[0]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(context['user'].image) > 0:
                os.remove(context['user'].image.url)
                image = request.FILES['image']
        model = Models.objects.get(id = request.POST['model'])
        seasson = Seasson.objects.get(id = request.POST['seasson'])
        car_types = CarTypes.objects.get(id = request.POST['car_types'])
        SCP = SetCharesteristicProduct.objects.get(id = request.POST['SCP'])
        country_manu = CountryManufacter.objects.get(id = request.POST['country_manu'])
        price = request.POST['price']
        description = request.POST['description']
        
        context['product'].model = model
        context['product'].seasson = seasson
        context['product'].SCP = SCP
        context['product'].country_manu = country_manu
        context['product'].price = price
        context['product'].description = description
        context['product'].save()    
    return render(request,'product/update.html',context)

def list_product(request):
    context = {}
    context['all_model'] = Product.objects.all().order_by("-id")
    return render(request,'product/list_product.html',context)

def detail_product(request,pk):
    context = {}
    context['product'] = Product.objects.filter(id=pk)[0]   
    return render(request,'product/detail.html',context)

def delete_product(request,pk):
    context = {}
    context['product'] = Product.objects.filter(id=pk)[0]
    context['product'].delete()   
    return redirect('list_product')
    