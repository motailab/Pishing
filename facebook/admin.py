from django.contrib import admin
from .models import Victim, Target, VisitorInfo

# Register your models here.
admin.site.register(Victim)
admin.site.register(Target)
admin.site.register(VisitorInfo)