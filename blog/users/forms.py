from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class Signup(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
   
    class Meta :
        model = User
        fields = ('email', 'first_name', 'last_name','username','password1','password2')
    
    def __init__(self,*arg, **kwargs):
      super(Signup,self).__init__(*arg, **kwargs)

      self.fields['username'].widget.attrs['class']='form-control'
      self.fields['password1'].widget.attrs['class']='form-control'
      self.fields['password2'].widget.attrs['class']='form-control'
        

class Editprofile(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'readonly': 'readonly'}))
    is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_super=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'readonly': 'readonly'}))
   
    class Meta :
        model = User
        fields = ('email', 'first_name', 'last_name','username','last_login','is_superuser','is_staff','date_joined','is_active','password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['is_superuser'].help_text = 'Designates that this user has all permissions without explicitly assigning them.'
        self.fields['is_staff'].help_text = 'Designates whether the user can log into this admin site.'
        self.fields['email'].help_text = 'To change your password, use the password change form.'

    
class Passwordchange(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'})
    )
