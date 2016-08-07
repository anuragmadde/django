from rest_framework.serializers import (
	ModelSerializer , 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,	
	EmailField,
	CharField,
	)

from comments.models import Comment
from blog.models import Blog
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model
from django.db.models import Q

User=get_user_model()
		

class UserCreateSerializer(ModelSerializer):
	email=EmailField(label="Email Address")
	email2=EmailField(label="Confirm Email")
	class Meta:
		model=User
		fields=[
			'username',
			'password',
			'email',
			'email2',
		]

		extra_kwargs = {
			"password":{"write_only":True},
			
		}



	def validate_email2(self,value):
		data = self.get_initial()
		email = data.get('email')
		email2=value
		if email != email2:
			raise ValidationError("Your emails should match")
		user_qs=User.objects.filter(email=email)
		if user_qs.exists():
			raise ValidationError("This email is already registered")
		return value

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		email    = validated_data['email']
		user_obj = User (
				username = username,
				email	 = email,

			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data


class UserLoginSerializer(ModelSerializer):
	token=CharField(allow_blank=True, read_only=True)
	username=CharField(allow_blank=True,required=False)
	email=EmailField(label="Email Address",allow_blank=True,required=False)
	class Meta:
		model=User
		fields=[
			'username',
			'password',
			'email',
			'token',
		]

		extra_kwargs = {
			"password":{"write_only":True},
			
		}



	def validate(self,data):
		user_obj=None
		username = data.get('username')
		print ('Username :'+username)
		email = data.get('email')
		print ("Email : "+email)
		password=data['password']
		if not email or not username:
			raise ValidationError("Username and Email are required to login !!")
		user=User.objects.filter(
				Q(email=email) &
				Q(username=username)
			).distinct()
		user=user.exclude(email__isnull=True)
		print (user)
		if user.exists() and user.count() ==1:
			user_obj=user.first()
		else:
			raise ValidationError("Not a valid Username/email.")

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Please provide valid credentials.")

		data['token'] = "SAMPLE TOKEN"

		return data

	