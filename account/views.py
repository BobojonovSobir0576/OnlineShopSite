from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.contrib import messages
from account.models import *
from account.forms import *

def signUpView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            return redirect('sign_in')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form': form})

def signInView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('justUser')
    return render(request,'login.html')

@login_required
def justUser(request):
    context = {}
    context['request_user'] = request.user
    return render(request,'user_detail.html',context)

@login_required
def justUserDetail(request,pk):
    justUser = User.objects.filter(pk=pk)[0]
    form = UserEditForm(instance = justUser)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = justUser)
        if form.is_valid():
            form.save()
            messages.success(request, "User Updated successfully." )
            return redirect('justUser')
    return render(request,'user_edit.html',{'form':form})

def logoutView(request):
    logout(request)
    return redirect('sign_in')