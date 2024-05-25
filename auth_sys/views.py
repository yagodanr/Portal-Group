from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import MyUserCreationForm
from .models import MyUser

# Create your views here.

class CustomLoginView(LoginView):
    model = MyUser
    template_name = 'auth_sys/login.html'
    redirect_authenticated_user = True
    
class CustomRegistrationView(CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name="auth_sys/register.html"
    success_url = reverse_lazy('login-form')

        
    
   
