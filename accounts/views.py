from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserRegisterForm

# Create your views here.


def account_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Cuenta creada, bienvenido al blog {username}!")
            return redirect("login")

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request,"accounts/register.html", context)
    


def account_profile(request):
    return render(request,"accounts/profile.html")
    



