"""anisongdb URL Configuration

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
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns


from .views import home, home_files

admin.autodiscover()

urlpatterns = [
    # Admin Urls
    url(r'^$', home, name="home"),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
    		home_files, name='home-files'),

    url(r'i18n/', include("django.conf.urls.i18n")),

    # local Accounts
    url(r'^accounts/', include("apps.accounts.urls")),
    # All Auth Urls
    url(r'^accounts/', include("allauth.urls")),
    ]

urlpatterns += i18n_patterns(
	url(r'^$', home, name= "home"),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()