from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .functions import random_pass, allowed_password
from .models import Car, Details, User_profile
from datetime import date
# Create your views here.


@login_required(login_url='accounts/login/')
def home(request):
    # return redirect('password_change')
    return render(request,'home.html')


def gallery(request):
    cars = Car.objects.all()
    data = {'cars':cars}
    return render(request, 'gallery.html', data)

def car(request):
    cars = Car.objects.all()
    data = {'cars':cars}
    return render(request,'car.html', data)

def detail(request, id):
    details = Details.objects.get(pk=id)
    cars = Car.objects.get(pk=id)
    data = {'details':details, 'cars':cars}
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        today = date.today()
        today = today.strftime("%y-%m-%d")
        if today > date_from or today > date_to or date_from > date_to:
            print('wrong choose')
            return redirect('detail', id = details.id)
        print(today)
        if date_from != '' and date_to != '':
            print('choose dates')
            return redirect('detail', id = details.id)
    return render(request,'detail.html', data)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if allowed_password(str(password), str(password_2)):
            try:
                username_db = User.objects.filter(username=username).first()
                email_db = User.objects.filter(email=email).first()
            except ObjectDoesNotExist:
                username_db = None  
                email_db = None  
            if username_db == None and email_db == None:
                User.objects.create_user(username, email, password)
                print('created')
                account = User.objects.get(username=username)
                user_profile = User_profile(user=account)
                user_profile.save()
                return redirect('log_to_account')
            else:
                print('username or email already exists in our database')
                return redirect('register')
        else:
            return redirect('register')
    return render(request, 'register.html')


def log_to_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('log_to_account')


def error_404(request, exception):
   context = {}
   return render(request,'404.html', context)

def error_500(request):
    context = {}
    return render(request,'500.html', context)

# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             email_db = User.objects.filter(email=email).first()
#         except ObjectDoesNotExist:
#             email_db = None
#         if email_db == None:
#             print('This account does not exists') 
#             return redirect('register')       
#         password = random_pass()
#         send_mail('Password', 'This is new password: '+ str(password), 'appmail@sendto.com', [email] )
#         return redirect('check_code', password=password)
#     return render (request, 'forgot_password.html')



# def check_code(request, password):
#     return render(request,'check_code.html', password)