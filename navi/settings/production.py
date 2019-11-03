from navi.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'navi',
                'USER': 'navi',
                'PASSWORD': 'Vsdo7MUtZVohBx6dximgN5NdXUisGt6n',
                'HOST': 'dpg-bmv0tsvd1hnnvsqk69o0',
                'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['*']
