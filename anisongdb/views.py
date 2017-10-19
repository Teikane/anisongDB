# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime

# Handles rending of pages

def home(request):
	today = datetime.date.today()
	return render(request, "anisongdb/index.html", {'today':today, 'now':now()}) 

def home_files(request, filename):
	return render(request, filename, {}, content_type="text/plain")