from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Message, Page, Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput())
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput())
    
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")
    
    class Meta:
        model = User
        fields= ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["reciever", "content"]
        
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'subtitle', 'body', 'autor', 'image')
        
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form_control'}),
            'subtitle' : forms.TextInput(attrs={'class': 'form_control'}),
            'body' : forms.TextInput(attrs={'class': 'form_control'}),
        }
        

class AvatarForm(forms.Form):
    image = forms.ImageField(label="Nueva imagen")

class PasswordSwapForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña vieja:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="Contraseña nueva:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Repetir contraseña:", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')