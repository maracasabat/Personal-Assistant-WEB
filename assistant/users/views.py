from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user


# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect("main:homepage")
        else:
            for error in list(form.errors.values()):
                print('error', messages.error)
                messages.error(request, error)
            #
            # messages.error(request, "Invalid form data")

    else:
        form = UserRegistrationForm()

    return render(request=request, template_name="auth/register.html", context={"form": form})


@unauthenticated_user
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("main:homepage")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserLoginForm()

    return render(
        request=request,
        template_name="auth/login.html",
        context={"form": form}

    )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('main:homepage')