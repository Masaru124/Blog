from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import Signup,Editprofile, Passwordchange
from newblog.models import Userprofile

class UserRegister(generic.CreateView):
    form_class = Signup
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')  

class UserEdit(generic.UpdateView):
    form_class = Editprofile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')  
    def get_object(self):
        return self.request.user
    
class PasswordChange(PasswordChangeView):
    form_class = Passwordchange
    success_url = reverse_lazy('password_sucess')
def password_sucess(request):
  return render(request,'registration/password_success.html',{})


class Showprofile(DetailView):
    model = Userprofile
    template_name = 'registration/user_profile.html'
    def get_context_data(self,*args, **kwargs):
       users=Userprofile.objects.all()
       context = super(Showprofile, self).get_context_data(*args, **kwargs)
       page_user=get_object_or_404(Userprofile,id=self.kwargs['pk'])


       context["page_user"]=page_user
       return context