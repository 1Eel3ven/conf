from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'), 
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'), 
    path('categories/<int:pk>/', views.CategoryView, name='category'), 
    path('about/', views.AboutView, name='about'), 
]