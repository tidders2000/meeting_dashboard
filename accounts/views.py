from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileForm

from .models import Profile
from db.views import finance, hr

from datetime import datetime
from datetime import date

from django.template.context_processors import csrf


def index(request):

    if request.user.is_authenticated:
        return redirect(reverse('finance'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)

            if user is not None:
                auth.login(request=request, user=user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('finance'))
            else:

                messages.error(request, "oops")
                messages.error(request, user)
                # redirects to switcher instead of dash to set group and business

    else:
        login_form = UserLoginForm()

    return render(request, 'index.html', {'login_form': login_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect('index')

# def login(request):
#     """Return a login page"""
#     if request.user.is_authenticated:
#         return redirect(reverse('index'))
#     if request.method == "POST":
#         login_form = UserLoginForm(request.POST)
#         if login_form.is_valid():
#             user = auth.authenticate(username=request.POST['username'],
#                                      password=request.POST['password'])

#             if user:
#                 auth.login(user=user, request=request)
#                 messages.success(request, "You have successfully logged in")
#                 """return redirect(reverse('index'))"""
#             else:
#                 login_form.add_error(None, 'your u or p is wrong')
#     else:
#         login_form = UserLoginForm()
#     return render(request, 'login.html', {'login_form': login_form})


@login_required
def registration(request):

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        telephone = request.POST.get("telephone", "default")
        image = request.FILES.get("profile_image")

        if registration_form.is_valid() and profile_form.is_valid():
            xe = registration_form.save()
            xe.profile.telephone = telephone
            xe.profile.profile_image = image
            xe.save()
            return redirect(reverse('new_business'))

    registration_form = UserRegistrationForm()
    profile_form = ProfileForm()
    return render(request, 'registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


@login_required
def user_profile(request):
    """the users profile page"""
    instance = Profile.objects.get(pk=request.user.pk)
    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=instance)
        form.save()
        return redirect(reverse('index'))
        messages.error(request, "Profile Updated")

    profile = ProfileForm(instance=instance)
    return render(request, 'profile.html', {'profile': profile, 'instance': instance})
