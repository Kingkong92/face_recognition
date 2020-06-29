from .base import *

SECRET_KEY = 'pry*u!kaw2@q1c5@)_yum)2!fymw+)f!0sj3jg9ngsh-jbgyc^'

DEBUG = True # 추후에 False로 변경 예정

ALLOWED_HOSTS = [
    '.compute.amazonaws.com',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')