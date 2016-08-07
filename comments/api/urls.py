from django.conf.urls import include, url
from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    # CommentEditAPIView,
    CommentCreateAPIView,
    )

urlpatterns = [
    # Examples:
     
     url(r'^$',CommentListAPIView.as_view(), name='list'),
     url(r'^create/',CommentCreateAPIView.as_view(), name='create'),
     url(r'^(?P<id>\d+)$',CommentDetailAPIView.as_view(), name='thread'),
     # url(r'^(?P<pk>\d+)/edit$',CommentEditAPIView.as_view(), name='edit'),
     
]

