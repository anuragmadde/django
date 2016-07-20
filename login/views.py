from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def login_view(request):
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")

	context = {
		"form":form,
		"title":"Login Page"
	}

	return render(request,"login.html",context)

def register_view(request):
	return render(request,"register.html",{})

def logout_view(request):
	return render(request,"logout.html",{})
