from django.shortcuts import render,redirect
from .forms import CreateUserForm,LoginForm
from  django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'crm/index.html')
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context={'form':form}    
    return render(request,"crm/register.html",context=context) 





def my_login(request):
    form = LoginForm()
    if request.method=='POST':
        form = LoginForm(request,data = request.POST)
        if  form.is_valid():
            username = request.POST.get('username')
            password = request.POST['password']
            user =authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                form.add_error(None,'Invalid Username or Password')
    context={"form":form}
    return render(request,'crm/my-login.html',context)  
@login_required(login_url='my-login')
def dashbord(request):
    return render(request,'crm/dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect('')