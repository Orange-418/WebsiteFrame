import re

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

from .forms import RegisterForm

def register(request):
    # If the user is already authenticated, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('home')

    template = 'register.html'
    error_message = None

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = RegisterForm(request.POST)

        if form.is_valid():
            # Validate the username
            if len(form.cleaned_data['username']) < 5:
                error_message = 'Username must be at least 5 characters long.'
            # Validate the first and last name
            elif (
                    len(form.cleaned_data['first_name']) < 1 or
                    len(form.cleaned_data['last_name']) < 1
            ):
                error_message = 'First and last name must be at least 1 character long.'
            # Validate that the username is unique
            elif User.objects.filter(username=form.cleaned_data['username']).exists():
                error_message = 'Username already exists.'
            # Validate that the passwords match
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                error_message = 'Passwords do not match.'
            # Validate the password strength
            elif not re.match(
                    r'^(?=.*[!@#$%^&*])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[!@#$%^&*A-Za-z\d]{12,64}$',
                    form.cleaned_data['password']
            ):
                error_message = 'Password must be between 12 and 64 characters long, and contain one special character (! @ # $ % ^ & *), one uppercase letter, one lowercase letter, and one number.'
            else:
                # Save the user to the database
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'])
                user.save()
                # Login the user
                dj_login(request, user)

                # Redirect to the account page
                return HttpResponseRedirect('/account/')

        else:
            error_message = "Please enter all details."
    else:
        form = RegisterForm()

    return render(request, template, {'form': form, 'error_message': error_message})

def home(request):
    """
    Home page view. Renders the 'home.html' template.
    """
    return render(request, 'home.html')

def login(request):
    """
    Handle user login.
    """
    # If the user is already authenticated, redirect them to the home page
    if request.user.is_authenticated:
        return redirect('home')

    template = 'login.html'
    if request.method == 'POST':
        # Collect form data
        username = request.POST['username']
        password = request.POST['user_password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            dj_login(request, user)

            # Redirect to the account page
            return HttpResponseRedirect('/account/')
        else:
            return render(
                request,
                template,
                {
                    'error_message': 'Invalid login credentials.'
                }
            )

    return render(request, template)

def logout(request):
    """
    Handle user logout.
    """
    dj_logout(request)
    # Redirect to the home page
    return HttpResponseRedirect('/')

def account(request):
    """
    Display the user's account information.
    """
    # If the user is not authenticated, redirect them to the login page
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email
    }
    return render(request, 'account.html', context)

def about(request):
    """
    Render the about page.
    """
    return render(request, 'about.html')
