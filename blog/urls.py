from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<slug:slug>/edit/', views.category_update, name='category_update'),
    path('category/<slug:slug>/delete/', views.category_delete, name='category_delete'),
]