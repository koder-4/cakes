from .base import *


SECRET_KEY = '2&usy4x0va)x((=q&u2m2mi7r-#1(plp%2m9)r8meqlgww#o&&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
