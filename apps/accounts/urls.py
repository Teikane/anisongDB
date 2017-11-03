# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from apps.accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Account views
    url(r'^signup/$', accounts_views.signup, name="signup"),
	# Account Profiles
	url(r'^myprofile/$', accounts_views.myprofile, name="myprofile"),
	url(r'^myprofile/profile/$', accounts_views.profile, name="profile"),
	url(r'^myprofile/settings/$', accounts_views.settings, name="settings"),
	url(r'^myprofile/privacy/$', accounts_views.privacy, name="privacy"),
	url(r'^myprofile/social/$', accounts_views.social, name="social"),
	url(r'^accounts/login/$', auth_views.login, {"template_name": "anisongdb/login.html"}, name="login"),
    ]