from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomRegisterForm, CaptchaLoginForm
from users.models import DevUser
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse , reverse_lazy


class AccountCreationView(generic.CreateView):
  template_name='developers/sign_up.html'
  form_class = CustomRegisterForm
  success_url='/sign_in/'



class AuthSessionView(LoginView):
    template_name='developers/sign_in.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
        return reverse("home_page")



class DeveloperListView(generic.ListView):
    model = DevUser
    template_name = 'developers/developer_list.html'
    context_object_name = 'developer_list'



class SignOutView(LogoutView):
    next_page = reverse_lazy ('sign_in')



