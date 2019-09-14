from django.contrib.gis.geoip2 import GeoIP2
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
    g = GeoIP2()
    try:
        lat, lon = g.lat_lon(ip)
        v = VisitorInfo.objects.create(ip=ip, lat=lat, lon=lon)
        v.save()
    except Exception:
        print(f'this ip {ip} not found in database')
    

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