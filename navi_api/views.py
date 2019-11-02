from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def log(request):
    return JsonResponse(request.POST)
