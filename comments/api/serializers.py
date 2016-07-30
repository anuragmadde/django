from rest_framework.serializers import (
	ModelSerializer , 
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

from comments.models import Comment
 
		
class CommentListSerializer(ModelSerializer):
	
	user = SerializerMethodField()
	reply_count = SerializerMethodField()
	class Meta:
		model=Comment
		fields =[
		
		'id', 
		'user',
		'content_type',
		'object_id',
		'parent',
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