from rest_framework.generics import (
	ListAPIView , 
	RetrieveAPIView , 
	UpdateAPIView , 
	DestroyAPIView , 
	CreateAPIView , 
	RetrieveUpdateAPIView,
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.permissions import (
	IsAdminUser,
	AllowAny,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly
	)

from rest_framework.pagination import (
	PageNumberPagination,
	LimitOffsetPagination,
	)

from comments.models import Comment 

from blog.api.pagination import CustomLimitOffsetPagination , CustomPageNumberPagination

from blog.api.permissions import IsOwnerOrReadOnly

from django.db.models import Q

from rest_framework.mixins import (
	DestroyModelMixin,
	UpdateModelMixin,
	)

from .serializers import (
	CommentListSerializer,
	CommentDetailSerializer,
	create_comment_serializer,
	# CommentEditSerializer, 
	)

class CommentListAPIView(ListAPIView):
	serializer_class=CommentListSerializer
	filter_backends=[SearchFilter]
	search_fields = ['content']
	pagination_class = CustomPageNumberPagination#PageNumberPagination

	def get_queryset(self, *args, **kwargs):
		querySet_List=Comment.objects.all()#filter(parent=None)
		query=self.request.GET.get('query')
		if query:
			querySet_List = querySet_List.filter(
				Q(content__icontains=query) | 
				Q(user__first_name__icontains=query)
				).distinct()
		return querySet_List



class CommentCreateAPIView(CreateAPIView):
	queryset=Comment.objects.all()
	# serializer_class=BlogCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)

	def get_serializer_class(self):
		model_type=self.request.GET.get("type")
		slug=self.request.GET.get("slug")
		parent_id=self.request.GET.get("parent_id",None)
		return create_comment_serializer(model_type=model_type,slug=slug,parent_id=parent_id,user=self.request.user)

		

class CommentDetailAPIView(DestroyModelMixin,UpdateModelMixin,RetrieveAPIView):
	queryset=Comment.objects.all()
	serializer_class=CommentDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'id'
	permission_classes = [IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
	
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)

# class BlogUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset=Blog.objects.all()
# 	serializer_class=BlogCreateUpdateSerializer
# 	lookup_field = 'slug'
# 	lookup_url_kwarg = 'slug'

# 	permission_classes = [IsOwnerOrReadOnly]
	
# 	def perform_update(self, serializer):
# 		serializer.save(user=self.request.user)


# class BlogDeleteAPIView(DestroyAPIView):
# 	queryset=Blog.objects.all()
# 	serializer_class=BlogDetailSerializer
# 	lookup_field = 'slug'
# 	lookup_url_kwarg = 'slug'