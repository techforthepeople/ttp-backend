from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User

class EmtLevel(models.Model): 
    name = models.CharField(max_length = 225)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(EmtLevel, self).save(*args, **kwargs)


class EmtProfile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.CharField(max_length = 225)
    dob = models.DateTimeField(null=True, blank=True)
    level = models.ForeignKey(EmtLevel, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(EmtProfile, self).save(*args, **kwargs)



class StatusLog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    longitude = models.DecimalField(null=True, blank=True, max_digits=20, decimal_places=8)
    latitude = models.DecimalField(null=True, blank=True,max_digits=20, decimal_places=8)
    heart_rate = models.IntegerField(blank=True, null=True)
    #humidity is a percentage. 
    humidity = models.DecimalField(max_digits=9, blank=True, null=True, decimal_places=6)
    #Temp is in C in sensehat
    temperature = models.DecimalField(max_digits=9, blank=True, null=True, decimal_places=6)
    #Pressure is mBar
    pressure = models.DecimalField(max_digits=9, blank=True, null=True, decimal_places=6)
    gas = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return self.created 

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(StatusLog, self).save(*args, **kwargs)


