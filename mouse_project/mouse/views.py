from .models import Mouse, MouseBrand
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewsForm 
from .models import NewsArticle
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import NewsArticle

def home(request):
    return render(request, "home.html")

def con(request):
    return render(request, "contract.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    form = AuthenticationForm()  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            if user.username == "admin" and request.POST['password'] == "noon123":
                login(request, user)  
                return redirect('adminpage')  
            login(request, user)
            return redirect('home')      
    return render(request, "accounts/login.html", {'form': form})

@login_required
def admin_page(request):
    articles = NewsArticle.objects.all()  
    users = User.objects.all()  
    form = NewsForm()  
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('adminpage')

    return render(request, 'adminpage.html', {
        'users': users, 
        'form': form,
        'articles': articles  
    })

def logout_view(request):
    logout(request)
    return redirect('home')

def news(request):
    articles = NewsArticle.objects.all().order_by('-date_posted')
    return render(request, 'news.html', {'articles': articles})


@login_required
def edit_news(request, news_id):
    news = get_object_or_404(NewsArticle, id=news_id)  
    if request.method == "POST":
        news.title = request.POST['title']
        news.content = request.POST['content']
        news.save()
        return redirect('adminpage')  
    return render(request, 'edit_news.html', {'news': news})

@login_required
def delete_news(request, news_id):
    news = get_object_or_404(NewsArticle, id=news_id)
    news.delete()
    return redirect('adminpage')

def article_detail(request, id):
    article = get_object_or_404(NewsArticle, id=id)
    return render(request, 'article_detail.html', {'article': article})