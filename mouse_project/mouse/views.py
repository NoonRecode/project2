from .models import Mouse, MouseBrand
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.email = form.cleaned_data["email"]  
            user.save()  
            login(request, user)  
            return redirect("home")
        else:
            print(form.errors)  
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def logout_view(request):
    logout(request)  
    return redirect('login')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form = AuthenticationForm()  # กำหนด form ในทุกกรณี
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # ดึงผู้ใช้จากฟอร์มที่ผ่านการตรวจสอบแล้ว
            login(request, user)  # ทำการล็อกอินผู้ใช้
            return redirect('home')  # เปลี่ยนเส้นทางไปหน้าหลัก
        
    # ส่งฟอร์มให้กับเทมเพลตเมื่อเป็น GET request
    return render(request, "accounts/login.html", {'form': form})
