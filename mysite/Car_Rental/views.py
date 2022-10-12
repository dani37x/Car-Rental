from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .functions import allowed_password, days, database, dates, dates_to_rent, check_availability, reservation
from .models import Car, Details, User_profile, Car_availability
from datetime import date, datetime

# @login_required(login_url='accounts/login/')
def home(request):
    # database(first_day=1, last_day=31, month=10)
    # cars = Car.objects.get(pk=1)
    # car_name =  cars.name
    # availability = Car_availability.objects.filter(car__name=car_name)
    # for i in availability:
    #     print(i.car)
    return render(request,'home.html')


@login_required(login_url='/accounts/login/')
def account(request):
    user = User.objects.get( username = request.user.username)
    user_account = User_profile.objects.get( user = user)
    rented_cars = Car_availability.objects.filter( owner = user)
    photos_container = {}
    used_photos = []
    # today = date.today()
    # today = today.strftime("%Y-%m-%d")
    for car in rented_cars:
        photo = Car.objects.get(name=car.car)
        # day = car.date
        # print(day)
        if photo.photo.url not in used_photos:
        # if photo.photo.url not in used_photos and str(day) >= today:
            # print('heeeeeeeeeeeeeere',car.date)
            photos_container[car] = photo.photo.url
            used_photos.append(photo.photo.url)
    print(photos_container)
    data = {'user' : user, 'user_account': user_account, 'rented_cars': rented_cars, 'photos_container':photos_container}
    return render(request,'account.html', data)

def gallery(request):
    cars = Car.objects.all()
    data = {'cars':cars}
    return render(request, 'gallery.html', data)

def car(request):
    cars = Car.objects.all()
    data = {'cars':cars}
    return render(request,'car.html', data)

@login_required(login_url='/accounts/login/')
def detail(request, id):
    details = Details.objects.get(pk=id)
    cars = Car.objects.get(pk=id)
    available_dates = dates_to_rent(id=id) 
    data = {'details':details, 'cars':cars, 'available_dates':available_dates}
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        today = date.today()
        today = today.strftime("%Y-%m-%d")
        if dates(date_from=date_from, date_to=date_to, today=today) == False:
            messages.add_message(request, messages.ERROR, '[ERROR] WRONG DATES CHOICE')
            return redirect('detail', id=id)
        days_difference = days( date_from=date_from, date_to=date_to)
        start_date = int(date_from[-2:])
        end_date = int(date_to[-2:])
        counter = 0
        if check_availability( start_date=start_date,end_date=end_date,
         days_difference=days_difference,counter=counter, cars=cars) == False:
            return redirect('detail', id=id)
        price = days(date_to=date_from, date_from=date_to) * details.price_for_day*(-1) + details.price_for_day*2
        profile = User.objects.get( username = request.user.username)
        account = User_profile.objects.get( user = profile)
        if account.money < price:
            print('Sorry, you dont have enough money')
            messages.add_message(request, messages.ERROR, '[ERROR] NOT ENOUGH MONEY')
            return redirect('detail', id=id)
        else:
            reservation( start_date=start_date, end_date=end_date, cars=cars, profile=profile)
        account.money = account.money - price
        account.save()
        messages.add_message(request, messages.INFO, f'CONGRATULATIONS, YOU HAVE JUST RENTED THE {cars.name}')
        return redirect('detail', id=id)
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
                account = User.objects.get(username=username)
                user_profile = User_profile(user=account)
                user_profile.save()
                return redirect('log_to_account')
            else:
                messages.add_message(request, messages.ERROR, '[ERROR]  THIS USERNAME OR EMAIL ALREADY EXISTS IN OUR DATABASE')
                return redirect('register')
        else:
            messages.add_message(request, messages.ERROR, '[ERROR]  PASSWORD MUST HAVE CONTAINS AT LEAST 6 CHARACTERS WITH SPECIAL CHAR, NUMBER AND BIG CHAR. PASSWORD MUST BE EQUAL TO SECOND PASSWORD')
            return redirect('register')
    return render(request, 'register.html')


def log_to_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if login(request, user):
            return redirect('account')
        else:
            messages.add_message(request, messages.ERROR, '[ERROR]  WRONG EMAIL OR PASSWORD')
            return redirect('log_to_account')
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
