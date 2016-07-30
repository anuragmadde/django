from django.conf.urls import include, url
from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    )

urlpatterns = [
    # Examples:
     
     url(r'^$',CommentListAPIView, name='list'),
     url(r'^(?P<id>\d+)$',CommentDetailAPIView.as_view(), name='thread'),
     
]

