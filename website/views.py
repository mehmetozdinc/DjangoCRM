from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterUserForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
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
    

def customer_list(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request,'website/customer-list.html',{'records':records})
    else:
        messages.error(request,"lütfen Giriş Yapınız")
        return redirect('home')


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
    

def customer_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request,'website/record.html',{'record':record})
    else:
        messages.warning(request,"Lütfen bu sayfayı görüntülemek için giriş yapın!!!")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request,"Kayıt Başarılı Bir Şekilde Silindi!!!")
        return redirect('home')
    else:
        messages.warning(request,"Lütfen bu sayfayı görüntülemek için giriş yapın!!!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Kayıt Başarılı Bir Şekilde Eklendi!!!")
                return redirect('home')
        return render(request,'website/add-record.html',{'form':form})
    else:
        messages.warning(request,"Lütfen bu sayfayı görüntülemek için giriş yapın!!!")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Kayıt Başarılı Bir Şekilde Güncellendi!!!")
            return redirect('customer_record',pk)
        return render(request,'website/update-record.html',{'form':form,'current_record':current_record})
    else:
        messages.warning(request,"Lütfen bu sayfayı görüntülemek için giriş yapın!!!")
        return redirect('home')
