from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from account.models import *
import os


def signUpView(request):
    context = {}
    context['gender'] = Gender.objects.all()
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        gender = Gender.objects.get(id = request.POST.get('gender'))
        birthdate = request.POST.get('birthdate')
        photo = request.FILES.get('photo')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
               
        if first_name == "" or last_name == "" or phone_number == "" or birthdate == "" or photo == None:
            context['error'] = "Информация неполная"
            return render(request,'register.html',context) 
        
        check_email = User.objects.filter(username = username)
        if len(check_email) != 0:
            context['error'] = "Такой пользователь существует"
            return render(request,'register.html',context)
        
        create_user = User.objects.create(username = username, first_name = first_name,last_name = last_name,phone_number = phone_number,gender = gender,photo = photo,birthdate = birthdate)
        create_user.set_password(password1)
        create_user.is_active = False
        create_user.save()
        try: get_role = Group.objects.get(name="JUSTUSER")
        except Group.DoesNotExist: get_role = None
        create_user.groups.add(get_role)
        if create_user is not None:
            return redirect('sign_in')
        
    return render(request,'register.html',context)

def signInView(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
            context['error'] = "Информация не заполнена"
            return render(request,'login.html',context)
        user = authenticate(request,username=username,password=password)
        # Когда пользователь входит в систему, на странице входа проверяются их роли и отправляются на их страницы.
        if user is not None:
            login(request,user)
            if len(user.groups.all().filter(name='JUSTUSER'))!=0: 
                return redirect('justUser')
            else:
                context['error'] = "Доступ к этой системе запрещен"
                return render(request,'login.html',context)
        else:
            context['error']='Ошибка логина или пароля'
    return render(request,'login.html',context)

@login_required
def justUser(request):
    context = {}
    context['request_user'] = request.user
    return render(request,'user_detail.html',context)

@login_required
def justUserDetail(request,pk):
    context = {}
    context['user'] = User.objects.filter(id = pk)[0]
    context['gender'] = Gender.objects.all()
    if request.method=='POST':
        if len(request.FILES) != 0:
            if len(context['user'].photo) > 0:
                os.remove(context['user'].photo.url)
                photo = request.FILES['photo']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        gender = Gender.objects.get(id = request.POST.get('gender'))
        birthdate = request.POST.get('birthdate')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
               
        if first_name == "" or last_name == "" or phone_number == "" or birthdate == "" or photo == None:
            context['error'] = "Информация неполная"
            return render(request,'user_edit.html',context) 
        
        context['user'].first_name = first_name
        context['user'].last_name = last_name
        context['user'].phone_number = phone_number
        context['user'].gender = gender
        context['user'].birthdate = birthdate
        context['user'].set_password(password1)
        context['user'].username = username
        context['user'].save()
    return render(request,'user_edit.html',context) 

@login_required
def logoutView(request):
    logout(request)
    return redirect('sign_in')