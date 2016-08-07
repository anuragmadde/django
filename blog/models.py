from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from markdown_deux import markdown
from .utils import get_read_time
from django.utils.text import slugify
from django.utils.safestring import mark_safe

# Create your models here.
from comments.models import Comment

def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)

class Blog(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=40)
	# image = models.FileField(null=True,blank=True)
	slug=models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location,null=True,blank=True,width_field="width_field",height_field="height_field")
	width_field = models.IntegerField(default=0)
	height_field = models.IntegerField(default=0)
	content = models.TextField()
	read_time = models.TimeField(null=True,blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blog:detail", kwargs={"slug": self.slug})

	def get_api_url(self):
		return reverse("api:detail", kwargs={"slug": self.slug})

	def get_markdown(self):
		content = self.content
		mark_text = markdown(content)
		return mark_safe(mark_text) 

	@property
	def get_comment(self):
		instance=self
		return Comment.custom_filter.filter_by_instance(instance)

	@property
	def get_contentType(self):
		instance=self
		return ContentType.objects.get_for_model(instance.__class__)


	class Meta:
		ordering=["-timestamp","-updated"]

def create_slug(instance,new_slug=None):
	slug=slugify(instance.title)
	print (new_slug)
	if new_slug is not None:
		slug=new_slug
	qs=Blog.objects.filter(slug=slug).order_by('-id')
	exists=qs.exists()
	if exists:
		print (qs.first().id)
		new_slug="%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug




def pre_save_receiver(sender,instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)
	if instance.content:
		instance.read_time=get_read_time(instance.content)


pre_save.connect(pre_save_receiver,sender=Blog)