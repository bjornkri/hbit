from .base import *  # noqa

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['', ])
