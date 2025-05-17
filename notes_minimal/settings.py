SECRET_KEY = 'change-me'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'notes',
]

ROOT_URLCONF = 'notes_minimal.urls'

MIDDLEWARE = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DEBUG = True
ALLOWED_HOSTS = []

STATIC_URL = '/static/'
