# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


from apps.accounts.forms import SignUpForm


# Create your views here.
def signup(request):
	form = SignUpForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect("home")
		else:
			form = SignUpForm()
	return render(request, "anisongdb/signup.html", {"form":form})

def myprofile(request):
	return render(request, "anisongdb/myprofile.html", content_type="text")

def profile(request):
	return render(request, "anisongdb/profile.html", content_type="text")

def settings(request):
	return render(request, "anisongdb/settings.html", content_type="text")

def privacy(request):
	return render(request, "anisongdb/privacy.html", content_type="text")

def social(request):
	return render(request, "anisongdb/social.html", content_type="text")