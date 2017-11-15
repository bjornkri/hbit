"""hbit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

from habits.views import HabitListView
from actions.views import ActionListView, ActionCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HabitListView.as_view(), name='home'),
    url(
        r'^actions/create/(?P<habit_pk>[0-9a-f-]+)/$',
        ActionCreateView.as_view(),
        name='create'
    ),
    url(r'^actions/$', ActionListView.as_view(), name='actions'),
]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
