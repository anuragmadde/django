from django import forms

from .models import SignUp
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	email = forms.EmailField()
	name=forms.CharField(label="Your Name" , max_length=40)
	question=forms.CharField(label="Your Question" ,widget=forms.Textarea)
	captcha=CaptchaField()

class SignUpForm(forms.ModelForm):
	captcha=CaptchaField()
	class Meta:
		model=SignUp
		fields=['first_name','last_name','email']


	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base,provider=email.split("@")
		domain,extension=provider.split(".")
		if not domain in ("gmail","yahoo","hotmail","outlook"):
			raise forms.ValidationError("Enter a valid domain Idiot !!")
		if not extension in ("com","co.in"):
			raise forms.ValidationError("WTF !! Does this even exist. Enter again")
		return email
