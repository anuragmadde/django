from django import forms
from pagedown.widgets import PagedownWidget
from .models import Blog


class BlogForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model=Blog
		fields=[
			'title',
			'content',
			'image',
		 ]

	# def clean_email(self):
	# 	email=self.cleaned_data.get('email')
	# 	email_base,provider=email.split("@")
	# 	domain,extension=provider.split(".")
	# 	if not domain in ("gmail","yahoo","hotmail","outlook"):
	# 		raise forms.ValidationError("Enter a valid domain Idiot !!")
	# 	if not extension in ("com","co.in"):
	# 		raise forms.ValidationError("WTF !! Does this even exist. Enter again")
	# 	return email
