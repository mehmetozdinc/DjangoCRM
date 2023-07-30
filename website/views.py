from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Giriş Başarılı!")
            return redirect('home')
        else:
            messages.error(request,"Bu işte bir terslik var!!!")
            return redirect('home')
    else:
        return render(request,'website/home.html',{})



def logout_user(request):
    logout(request)
    messages.success(request,"Başarılı bir şekilde çıkış gerçekleştirildi!!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Kayıt Başarılı! Lütfen Giriş Yapınız!!!")
            return redirect('home')
        else:
            return render(request,'website/register.html',{'form':form})
    else:
        form = RegisterUserForm()
        return render(request,'website/register.html',{'form':form})
    
    