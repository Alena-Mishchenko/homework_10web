
from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:page>/', views.main, name='root_paginate'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('add_quote/', views.add_quote, name='add_quote'),
  
]