from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

# from blog.models import Blog
# Create your models here.

class BlogManager(models.Manager):

	def all(self):
		return super(BlogManager,self).filter(parent=None)

	def filter_by_instance(self,instance):
		content_type= ContentType.objects.get_for_model(instance.__class__)
		obj_id=instance.id
		qs=super(BlogManager,self).filter(content_type=content_type,object_id=obj_id).filter(parent=None)
		return qs

	def create_by_model_type(self , model_type , slug ,content,user,parent_obj=None):
		model_qs=ContentType.objects.filter(model=model_type)
		if  model_qs.exists() :
			somemodel=model_qs.first().model_class()
			obj_qs = somemodel.objects.filter(slug=slug)
			if obj_qs.exists() or obj_qs.count() ==1:
				instance=self.model()
				instance.content=content
				instance.user=user
				instance.content_type=model_qs.first()
				instance.object_id=obj_qs.first().id
				if parent_obj:
					instance.parent=parent_obj
				instance.save()
				return instance
		return None


class Comment(models.Model):

 	user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
 	# post = models.ForeignKey(Blog)

 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
 	object_id = models.PositiveIntegerField(null=True)
 	content_object = GenericForeignKey('content_type', 'object_id')
 	parent = models.ForeignKey("self",null=True,blank=True)

 	content = models.TextField(max_length=720)
 	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

 	def __str__(self):
 		return str(self.content)

 	def get_comments_absolute_url(self):
 		return reverse("comment:detail", kwargs={"id": self.id})

 	def get_comments_delete_url(self):
 		return reverse("comment:delete", kwargs={"id": self.id})


 	class Meta:
 		ordering = ["-timestamp"]

 	objects=models.Manager()
 	custom_filter=BlogManager()

	
 	def children(self):
 		return Comment.objects.filter(parent=self)

 	@property
 	def is_parent(self):
 		if self.parent is not None:
 			return False
 		return True
