from django.shortcuts import render
from navi_api.models import (
                    StatusLog,
                )
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.serializers import serialize


# Create your views here.

def log(request, user_id):
    user = User.objects.get(pk=user_id)
    StatusLog.objects.create(user = user, heart_rate=140, longitude=-73.9486327, latitude=40.8215284, humidity=float(request.POST['humidity']), temperature=float(request.POST['temperature']), pressure=float(request.POST['pressure']))
    return JsonResponse(request.POST)

def logs(request, user_id):
    user = User.objects.get(pk=user_id)
    user_logs = user.status_log_set.all()
    return JsonResponse(serialize('json', user_logs))
