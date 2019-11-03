from django.contrib import admin
from .models import (
    EmtLevel,
    EmtProfile,
    StatusLog,
)

# Register your models here.
admin.site.register(EmtLevel)
admin.site.register(EmtProfile)
admin.site.register(StatusLog)