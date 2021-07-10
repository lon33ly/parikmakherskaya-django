from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *

from .forms import CreateUserForm


# Create your views here.
def start_page(request):
    services_list = Service.objects.all()
    context = {'services_list': services_list}
    if request.user.is_authenticated:
        context['auth'] = True
    return render(request, 'index.html', context)


def services_page(request):
    services_list = Service.objects.all()
    context = {'services_list': services_list}
    if request.user.is_authenticated:
        context['auth'] = True
    return render(request, 'services.html', context)


def booking_page(request):
    context = {}
    if request.user.is_authenticated:
        context['date_list'] = Date.objects.all()
        context['time_list'] = Time.objects.all()
        context['master_list'] = Master.objects.all()
        context['auth'] = True

    if request.method == 'POST':
        date = request.POST.get("date")
        time = request.POST.get("time")
        master = request.POST.get("master")
        description = request.POST.get("description")

        preorder = PreOrder(reserved_date=date, reserved_time=time, master=master, description=description)
        preorder.save()

    return render(request, 'booking.html', context)


def masters_page(request):
    masters_list = Master.objects.all()
    context = {'masters_list': masters_list}
    if request.user.is_authenticated:
        context['auth'] = True

    return render(request, 'masters.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('start')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('start')
        messages.error(request, "Email или пароль введены неправильно")

    context = {}
    return render(request, 'login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('start')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except forms.ValidationError as ve:
                context = {'form': form, 'validation_errors': ve}
                return render(request, 'register.html', context)
            user = form.cleaned_data.get('email')
            messages.success(request, f"Аккаунт успешно зарегистрирован на почту {user}")

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    return redirect('start')


@login_required(login_url='login')
def account_page(request):
    orders = Order.objects.filter(customer=request.user)
    context = {'orders': orders}
    if request.user.is_authenticated:
        context['auth'] = True
    return render(request, 'account.html', context)
