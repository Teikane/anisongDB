# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.utils.timezone import now

from django.contrib.auth import login, authenticate
from .forms import SignUpForm
import datetime

# Handles rending of pages

def home(request):
	today = datetime.date.today()
	return render(request, "anisongdb/index.html", {'today':today, 'now':now()}) 

def home_files(request, filename):
	return render(request, filename, {}, content_type="text/plain")

def signup(request):
	form = SignUpForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect("/")
		else:
			form = SignUpForm()
	return render(request, "anisongdb/signup.html", {"form":form})