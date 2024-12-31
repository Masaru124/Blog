from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('',home.as_view(),name="home"),
    path('article/<int:pk>/',articledetail.as_view(),name="article-detail"),
    path('add_post/',addpost.as_view(),name = "add_post"),
path('article/edit/<int:pk>/', Updatepost.as_view(), name="update-post"),
path('article/<int:pk>/remove/', deletepost.as_view(), name="delete-post"),
    path('add_category/',AddCategory.as_view(),name = "add_category"),
    path('category/<str:cats>/', CategoryView, name='category'), 
    path('article/<int:pk>/like/', Like, name='like_post'), 
]

