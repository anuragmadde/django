from rest_framework.serializers import (
	ModelSerializer , 
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from blog.models import Blog

from comments.api.serializers import CommentListSerializer
from comments.models import Comment


class BlogCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model=Blog
		fields = [
			'title',
			'content',
		]

class BlogListSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
		view_name = "api:detail",
		lookup_field="slug",
		)

	user = SerializerMethodField()
	image = SerializerMethodField()
	comments = SerializerMethodField()
	class Meta:
		model=Blog
		fields = [
			'url',
			'user',
			'title',
			'image',
			'comments',
		]
		
	def get_user(self,obj):
		return str(obj.user.username)

	def get_image(self,obj):
		try:
			image = obj.image.url
		except:
			image=None
		return image

	def get_comments(self,obj):
		content_type = obj.get_contentType
		object_id = obj.id
		comment_query=Comment.custom_filter.filter_by_instance(obj)
		comment=CommentListSerializer(comment_query, many=True).data
		return comment
		

class BlogDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	
	class Meta:
		model=Blog
		fields = [
			'id',
			'user',
			'title',
			'slug',
			'content',
			'image',
			'timestamp',
			
		]	

	def get_user(self,obj):
		return str(obj.user.username)

	def get_image(self,obj):
		try:
			image = obj.image.url
		except:
			image=None
		return image

	
