import requests
from facebook.models import VisitorInfo

def saveVisitor(request):
    """
        this function save request user info into 
        database
        like
        ip address,
        lat, lon
    """
    ip = get_client_ip(request)
    try:
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey=219d18f6ba0b491ca1b4374c88110ee2&ip={ip}'
        response = requests.get(url);
        data = response.json()
        city = data['city']
        lat = data['latitude']
        lon = data['longitude']
        district = data['district']
        isp = data['isp']
        
        obj, created = VisitorInfo.objects.get_or_create(ip=ip)
        obj.city = city
        obj.lat = lat
        obj.lon = lon
        obj.district = district
        obj.isp = isp
        obj.save()

    except Exception as e:
        print(f'got exception {e}')
    

def get_client_ip(request):
    """
    this function extract ip address 
    from request header and return
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip