from django.urls import path
from navi_api.views import log

urlpatterns = [
    path('log', log, name='log'),
]
