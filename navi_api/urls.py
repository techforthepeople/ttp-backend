from django.urls import path
from navi_api.views import (log, logs)

urlpatterns = [
    path('log/<user_id>', log, name='log'),
    path('logs/<user_id>', logs, name='logs')
]
