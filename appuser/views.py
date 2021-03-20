from typing import ContextManager
from django.shortcuts import render, redirect
from .forms import CreateUser_Register
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .decorators import unauthenticated
# Create your views here.

# this method is for registration there is another registration method for api


@unauthenticated
def register(request):
    if request.method == 'POST':
        print("inside post")

        print("try")
        form = CreateUser_Register(request.POST)
        profile_form = ProfileForm(request.POST)
        print("formbefore")
        if form.is_valid() and profile_form.is_valid():
            print("isvalid ")
            user = form.save()
            profile_user = profile_form.save(commit=False)
            profile_user.user_author = user
            profile_user.save()
            print("username")
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            print("username=", password1)
            return redirect('loggin')
        else:
            return render(request, 'appuser/register.html', {'form': form, 'profile_form': profile_form})

    form = CreateUser_Register()
    profile_form = ProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'appuser/register.html', context)

# this method will log in to account


@unauthenticated
def loginAccount(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('email ', email, 'password ', password)
        username = User.objects.filter(email=email.lower()).first()
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = messages.info(
                request, "Username Or Password is incorrect")
            return render(request, 'appuser/login.html')

    return render(request, 'appuser/login.html')
