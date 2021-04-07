from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

from .forms import RegistrationForm, AccountAuthenticationForm
from .models import User, Car

def registration_view(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('userinfo')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context = {'registration_form': form}
    return render(request, 'avtoprokat/register.html', context)

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('userinfo')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect('userinfo')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'avtoprokat/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def addcar(request):
    if request.user.is_superuser and request.POST:
        name_en = request.POST['carname_en']
        name_ru = request.POST['carname_ru']
        created = request.POST['created']
        Car.objects.create(
            name_en=name_en,
            name_ru=name_ru,
            created=created,
            added=date.today(),
        )

    return render(request, 'avtoprokat/addcar.html')

@login_required
def addusercar(request):
    users = User.objects.order_by('email')
    cars = Car.objects.order_by('name_en')
    context = {'users': users, 'cars': cars}
    if request.user.is_superuser and request.POST:
        username = request.POST['username']
        user = User.objects.get(username=username)

        car_name = request.POST['cars']
        car = Car.objects.get(name_en=car_name)

        car.renter.add(user.id)

        subject = 'Аренда машины.'
        message = 'Вам арендована машина {}.'.format(car_name)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail( subject, message, email_from, recipient_list, fail_silently=False)

    return render(request, 'avtoprokat/addusercar.html', context)

@login_required
def userinfo(request):
    current_user = request.user
    user = User.objects.filter(id=current_user.id)
    context = {'user': user}

    return render(request, 'avtoprokat/userinfo.html', context)

@login_required
def edituserinfo(request):
    current_user = request.user
    user = User.objects.filter(id=current_user.id)
    if request.POST:
        user.update(
            email=request.POST['email'],
            username=request.POST['username'],
            language=request.POST['language'],
        )

    return render(request, 'avtoprokat/edituserinfo.html')
