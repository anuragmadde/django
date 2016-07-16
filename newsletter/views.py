
from django.conf import settings

from django.core.mail import send_mail

from django.shortcuts import render

from .forms import SignUpForm,ContactForm

from .models import SignUp

# Create your views here.
def contact(request):
	title= "Hey Dude !!"

	form = ContactForm()

	context = {
		"title" : title,
		"form"	: form,
	}
	
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_name  = form.cleaned_data.get("name")
		form_question = form.cleaned_data.get("question")
		
		form.save()

		subject = 'Contact Form'
		from_email =  settings.EMAIL_HOST_USER
		recipient_list = [from_email , form_email]
		message = "Hi"
		new_html_message = " <h2>This is in response to your Query</h2> "

		send_mail (subject , message , from_email ,['anuragmadde@hotmail.com'] ,fail_silently = False,)
	
	return render(request,"contact.html",context)




def home(request):
	title= "Whats Up MaDDe !!"

	form = SignUpForm(request.POST or None)	

	context = {
		"title" : title,
		"form"	: form,
	}
	
	if form.is_valid():
		instance = form.save()

		subject = 'Contact Form'
		from_email =  settings.EMAIL_HOST_USER
		# recipient_list = [from_email , instance.email]
		message = "Hi"
		new_html_message = " <h2>This is in response to your Query</h2> "

		send_mail (subject , message , from_email ,['anuragmadde@hotmail.com'] ,fail_silently = False,)  

		context = {

			"title" : "Thanks %s for Signing Up. You will receive an email to %s  soon " %(instance.first_name,instance.email)
		}


	if request.user.is_authenticated():

		# print(SignUp.objects.all())

		queryset = SignUp.objects.all()
		context = {
			"queryset": queryset
		}
		
	
	return render(request,"home.html",context)


def about(request):
	return render(request,"about.html",{})