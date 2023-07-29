from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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
    pass