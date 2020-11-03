from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import auth, messages
from accounts.models import Account
from django.contrib.auth.mixins import LoginRequiredMixin


# class HomeView(TemplateView):
#     template_name = 'accounts/base.html'


def changePasswordView(request, email):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = Account.objects.get(email=email)
            user.set_password(password1)
            return redirect('/todo')
        else:
            messages.error(request, "Password are not matching")
            return redirect('/changepassword')

    else:
        return render(request, 'accounts/changepassword.html')


def logoutView(request):
    auth.logout(request)
    return redirect('/')


def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            email=email,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('myApp:mytodo_list')
        else:
            messages.error(request, "Invalid Username/Password")
            return redirect('/')
    else:
        return render(request, 'accounts/login.html')


def signupView(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Account.objects.filter(email=email).exists():
                messages.error(request, "email id already exists")
                return redirect('/signup')
            if Account.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect('/signup')
            else:
                user = Account.objects.create_user(
                    email=email,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    DOB=dob,
                    password=password1
                )
                user.save()
                messages.info(request, "Account has been created successfully")
                return redirect('/')
        else:
            messages.error(request, "Passwords are not matching")
            return redirect('/signup')

    else:
        return render(request, 'accounts/signup.html')
