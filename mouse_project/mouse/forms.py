from django import forms
from .models import Mouse
from .models import NewsArticle
from .models import NewsArticle
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="อีเมล", widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # เพิ่ม email เข้าไป


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'image']
