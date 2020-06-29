from .base import *
from decouple import config


SECRET_KEY = config('SECTRTE_KEY')

DEBUG = True

ALLOWED_HOSTS = []