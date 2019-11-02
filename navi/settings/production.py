from navi.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'adapto_qu66',
                'USER': 'adapto',
                'PASSWORD': 'L8f5UOnL5t',
                'HOST': 'dpg-blq3la4o8crha3ep3590',
                'PORT': '5432',
    }
}

SECRET_KEY = 'w2p!z93l004jbhl_$-k0_q^znvqo3acvkbffth+!ah)96xd@h4'
