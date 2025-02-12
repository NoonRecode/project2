from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import admin_page, edit_news, delete_news

urlpatterns = [
    path('',views.home, name='home'),
    path('contract/',views.con, name='contract'),
    path('login/',views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('adminpage/', views.admin_page, name='adminpage'),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.article_detail, name='article-detail'),
    path('edit_news/<int:news_id>/', edit_news, name='edit_news'),
    path('delete_news/<int:news_id>/', delete_news, name='delete_news'),
    
]
