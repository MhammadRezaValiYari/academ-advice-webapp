from django.shortcuts import render, redirect
from registration.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
# Create your views here.

# home reverse page


def home(request):
    return render(request, 'main/index.html')

# system Login


# system Logout


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# registering system


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False, clean=True)
            profile.user = user
            registered = True

            login(request, user)
            return redirect(reverse('dashboard:dashboard'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()

        profile_form = UserProfileInfoForm()

    Context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }
    return render(request, 'main/registration.html', Context)


# Login view


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dashboard:dashboard')
    else:
        return render(request, 'main/login.html')


# change password function


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Good Job')
            return redirect(reverse('dashboard:dashboard'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html', {
        'form': form
    })
