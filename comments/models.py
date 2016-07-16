from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from blog.models import Blog
# Create your models here.

class BlogManager(models.Manager):
	def filter_by_instance(self,instance):
		content_type= ContentType.objects.get_for_model(instance.__class__)
		obj_id=instance.id
		qs=super(BlogManager,self).filter(content_type=content_type,object_id=obj_id)
		return qs


class Comment(models.Model):

 	user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
 	# post = models.ForeignKey(Blog)

 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
 	object_id = models.PositiveIntegerField(null=True)
 	content_object = GenericForeignKey('content_type', 'object_id')

 	comment = models.TextField(max_length=720)
 	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

 	def __str__(self):
 		return str(self.comment)

 	objects=models.Manager()
 	custom_filter=BlogManager()

	
