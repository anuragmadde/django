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

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


from comments.models import Comment 

from blog.api.pagination import CustomLimitOffsetPagination , CustomPageNumberPagination

from blog.api.permissions import IsOwnerOrReadOnly

from django.db.models import Q

from rest_framework.mixins import (
	DestroyModelMixin,
	UpdateModelMixin,
	)

from .serializer import (
	UserCreateSerializer ,
	UserLoginSerializer
	)

from django.contrib.auth import get_user_model

User=get_user_model()

class UserCreateAPIview(CreateAPIView):
	serializer_class=UserCreateSerializer
	queryset=User.objects.all()

class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class=UserLoginSerializer

	def post(self, request, *args,**kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			return Response(serializer.data,status=HTTP_200_OK)
		return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
