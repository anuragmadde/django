from rest_framework.serializers import (
	ModelSerializer , 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,	
	)

from comments.models import Comment
from blog.models import Blog
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth import get_user_model

User=get_user_model()
		

def create_comment_serializer(model_type=None,slug=None,parent_id=None,user=None):
	class CommentCreateSerializer(ModelSerializer):
		class Meta:
			model=Comment
			fields= [
				'id',
				'content',
				'timestamp',
			]
		def __init__(self,*args,**kwargs):
			self.model_type=model_type
			self.slug=slug
			self.parent_obj= None
			if parent_id:
				parent_qs = Comment.objects.filter(id=parent_id)
				if parent_qs.exists() and parent_qs.count !=1:
					self.parent_obj=parent_qs.first()
			return super(CommentCreateSerializer,self).__init__(*args,**kwargs)

		def validate(self, data):
			model_type=self.model_type
			model_qs=ContentType.objects.filter(model=model_type)
			if not model_qs.exists() or model_qs.count() != 1 :
				raise ValidationError("Not a valid Content Type")
			somemodel=model_qs.first().model_class()
			obj_qs = somemodel.objects.filter(slug=self.slug)
			if not obj_qs.exists() or obj_qs.count() !=1:
				raise ValidationError("The slug for this content type does not exist")
			return data

		def create(self,validated_data):
			content=validated_data.get("content")
			if user:
				my_user=user
			else:
				my_user=User.objects.all().first()
			model_type=self.model_type
			slug=self.slug
			parent_obj=self.parent_obj
			comment=Comment.custom_filter.create_by_model_type(model_type,slug,content,my_user,parent_obj)
			return comment

	return CommentCreateSerializer


class CommentListSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
		view_name = "api-comment:thread",
		lookup_field = 'id',
		)
	
	user = SerializerMethodField()
	reply_count = SerializerMethodField()
	class Meta:
		model=Comment
		fields =[
		'url',
		'id', 
		'user',
		# 'content_type',
		# 'object_id',
		# 'parent',
		'content',
		'reply_count',
		'timestamp',
		]

	def get_user(self,obj):
		return str(obj.user.username)

	def get_reply_count(self,obj):
		if obj.is_parent:
			return obj.children().count()
		return 0



class CommentChildSerializer(ModelSerializer):
	class Meta:
		model=Comment
		fields = [
			'id',
			'content',
			'timestamp',
		]

class CommentDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	replies = SerializerMethodField()
	reply_count = SerializerMethodField()
	detail_url = SerializerMethodField()
	class Meta:
		model=Comment
		fields = [
			'id',
			'user',
			'content_type',
			'object_id',
			'parent',
			'content',
			'timestamp',
			'replies',
			'reply_count',
			'detail_url',
		]	

		read_only_fields=[
			'content_type',
			'object_id',
			'parent',
			'reply_count'
			'replies',
		]

	def get_user(self,obj):
		return str(obj.user.username)

	def get_replies(self,obj):
		if obj.is_parent:
			return  CommentChildSerializer(obj.children(),many=True).data
		return None
	
	def get_reply_count(self,obj):
		if obj.is_parent:
			return obj.children().count()
		return 0

	def get_detail_url(self,obj):
		try:
			return obj.content_object.get_api_url()
		except:
			return None



	