from navi.settings.base import *

DEBUG=True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'navi',
                'USER': 'navi',
                'HOST': '127.0.0.1',
                'PORT': '5432',
    }
}

