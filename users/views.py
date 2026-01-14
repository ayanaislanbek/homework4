from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomRegisterForm, CaptchaLoginForm
from users.models import DevUser



def account_creation_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/sign_in/')
    else:
        form = CustomRegisterForm()
    return render(
        request,
        template_name='developers/sign_up.html',
        context={'form': form}
    )



def auth_session_view(request):
    if request.method == 'POST':
        form = CaptchaLoginForm (data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/developer_list/')
    else:
        form =CaptchaLoginForm()
    
    return render(
        request,
        template_name='developers/sign_in.html',
        context={'form': form}
    )




def developer_list_view(request):
    if request.method == 'GET':
        developer_list = DevUser.objects.all()
    return render(
        request,
        template_name='developers/developer_list.html',
        context={'developer_list': developer_list}
    )



def sign_out_view(request):
    logout(request)
    return redirect('/sign_in/')
