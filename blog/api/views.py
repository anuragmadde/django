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

from blog.models import Blog 

from .pagination import CustomLimitOffsetPagination , CustomPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from django.db.models import Q

from .serializer import (
	BlogListSerializer , 
	BlogDetailSerializer , 
	BlogCreateUpdateSerializer,
	)

class BlogListAPIView(ListAPIView):
	serializer_class=BlogListSerializer
	# serializer = BlogListSerializer(data=request.data,context={'request':request})
	filter_backends=[SearchFilter]
	search_fields = ['title']
	pagination_class = CustomPageNumberPagination#PageNumberPagination

	def get_queryset(self, *args, **kwargs):
		querySet_List=Blog.objects.all()
		query=self.request.GET.get('query')
		if query:
			querySet_List = querySet_List.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) | 
				Q(user__first_name__icontains=query)
				).distinct()
		return querySet_List



class BlogCreateAPIView(CreateAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogCreateUpdateSerializer
	permission_classes = [IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class BlogDetailAPIView(RetrieveAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'


class BlogUpdateAPIView(RetrieveUpdateAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogCreateUpdateSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'

	permission_classes = [IsOwnerOrReadOnly]
	
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)


class BlogDeleteAPIView(DestroyAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogDetailSerializer
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'