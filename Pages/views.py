from datetime import datetime
from django.forms.models import BaseModelForm
from django.http import HttpResponse

from django.shortcuts import render
from Pages.models import *
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from Pages.forms import PasswordSwapForm


from Pages.forms import *

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'Pages/home.html'
    
    
#CRUD PAGINAS

class PageList(LoginRequiredMixin, ListView):
    model = Page
    context_object_name = 'page'
    template_name = "Pages/page_list.html"
    
class PageDetail(LoginRequiredMixin, DetailView):
    model = Page
    context_object_name = 'page'
    template_name = "Pages/page_detail.html"

    
class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("PageList")
    template_name = 'Pages/page_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PageCreate, self).form_valid(form)
    
    
class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = "Pages/page_edit.html"
    success_url = reverse_lazy("PageList")
    fields = ['title', 'subtitle', 'body', 'image']
    
class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("PageList")
    template_name = "Pages/page_delete.html"


#PERFIL Y LOGIN


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                
                return render(request, "Pages/home.html", {})
            else:
                return render(request, "Pages/home.html", {})
            
        else:
            return render(request, "Pages/home.html", {})
        
    form = AuthenticationForm()
        
    return render(request, "Pages/login.html", {'form' : form })
    
def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Pages/home.html", {})
    else:
        form = UserRegisterForm()
    return render(request, "Pages/register.html", {'form':form})

@login_required
def profile(request):
    
    user = request.user
    avatar = Avatar.objects.filter(user = user.id)
    
    if avatar:
        context  = avatar[0].image.url
    else: 
        context = avatar
    
    return render(request, 'Pages/profile.html', {'user': user, 'avatar' : context})


@login_required
def editProfile(request):
    user = request.user
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            user.email = info['email']
            user.password1 = info['password1']
            user.password2 = info['password1']
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.save()
            
            return render(request, "Pages/profile.html")
    else:
        form = UserEditForm()
    
    return render(request, "Pages/profile_edit.html", {'form': form, 'user': user})

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordSwapForm
    template_name = "Pages/password_change.html"
    success_url = reverse_lazy("Profile")
    
@login_required
def avatarChange(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            
            u = User.objects.get(username=request.user)
            avatar = Avatar(user = u, image = form.cleaned_data['image'])
            
            avatar.save()
            
            return render(request, 'Pages/profile.html', {})
    else:
        form = AvatarForm()
        
    return render(request, 'Pages/avatar_change.html', {'form': form})





#MENSAJES

@login_required
def messages(request):
    user = request.user
    
    messages = Message.objects.filter(reciever = user)
    
    return render(request, "Pages/messages.html", {'messages': messages})
    
    
@login_required
def send_message(request):
    user = request.user
    
    if request.method == "POST":
        form = MessageForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            message = Message(sender = user, reciever = info['reciever'], content = info['content'], date = datetime.now())
            message.save()
            
            return render(request, "Pages/home.html", {})
            
    else:
        form = MessageForm()

    return render(request, "Pages/send_message.html", {'form' : form})
    
def about(request):
    return render(request, "Pages/about.html")


        