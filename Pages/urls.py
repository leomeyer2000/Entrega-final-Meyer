from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Pages.views import *
from django.contrib.auth.views import LogoutView


import re

urlpatterns = [
    path('', Home.as_view(), name="Inicio"),
    path('pages/', PageList.as_view(), name="PageList"),
    path('pages/<int:pk>', PageDetail.as_view(), name="PageDetail"),
    path('pages/create', PageCreate.as_view(), name="PageCreate"),
    path('pages/update/<int:pk>', PageUpdate.as_view(), name="PageUpdate"),
    path('pages/delete/<int:pk>', PageDelete.as_view(), name="PageDelete"),
    
    path('accounts/login', login_request, name ="Login"),
    path('accounts/signup', register, name="Signup"),
    path('accounts/logout', LogoutView.as_view(template_name='Pages/logout.html'), name="Logout"),
    path('accounts/profile/', profile, name="Profile"),
    path('accounts/profile/edit', editProfile, name="EditProfile"),
    path('accounts/profile/avatar', avatarChange, name="AvatarChange"),
    path('accounts/profile/password', PasswordChange.as_view(), name="PasswordChange"),
    
    path('messages', messages, name="Messages"),
    path('messages/send', send_message, name="SendMessage"),
    
    path('about/', about, name='About'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)