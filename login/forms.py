from django import forms
# from pagedown.widgets import PagedownWidget


class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
	 