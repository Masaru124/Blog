from django.urls import path
from .views import UserRegister, UserEdit, PasswordChange, Showprofile
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name="edit_profile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordChange.as_view(), name="password-change"),
    path('password_sucess/', views.password_sucess, name="password_sucess"),
    path('<int:pk>/profile/', Showprofile.as_view(), name='show_profile'),
]