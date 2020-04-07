from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_7213_6ep77rl7i%fp3d%&!m6@#jsu3q$941tfnk%8a2ge-=fn'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

