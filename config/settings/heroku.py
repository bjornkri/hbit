from .base import *  # noqa

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['.herokuapp.com', '0.0.0.0'])
