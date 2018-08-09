from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditForm, ChangePasswordForm

# Create your views here.

def home(request):
    return render(request, "authentication/home.html", {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials. Please try again")
            return redirect('login')

    else:
        return render(request, "authentication/login.html")


def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            #form = SignUpForm()
            authenticate(request, username=username, password=password)
            messages.success(request, 'You have been successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'authentication/register.html', context)


def edit_profile(request):
    if request.method == "POST":
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            #form = EditForm()
            messages.success(request, 'Profile successfully updated')
            return redirect('home')
    else:
        form = EditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'authentication/edit_profile.html', context)


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password successfully updated')
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        context = {'form': form}
        return render(request, 'authentication/change_password.html', context)

