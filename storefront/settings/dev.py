from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-e9smuajjf9c*oxyyalnn#*b)e$w784m=c4r=qk_@3m26*af06g'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST' : 'localhost',
        'USER' : 'root',
        'PASSWORD': 'password'
    }
}