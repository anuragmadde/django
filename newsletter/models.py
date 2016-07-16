from django.db import models

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField()
	first_name=models.CharField(max_length=40)
	last_name=models.CharField(max_length=40)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updates_timestamp=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return self.first_name 
