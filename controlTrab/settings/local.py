from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR.child('static'),)
STATIC_ROOT = 'staticfiles'

#Se definae la ruta y la carpeta en la que se guardaran los archivos MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
