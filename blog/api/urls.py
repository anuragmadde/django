from django.conf.urls import include, url
from .views import (
    BlogListAPIView,
    BlogDetailAPIView,
    BlogUpdateAPIView,
    BlogDeleteAPIView,
    BlogCreateAPIView,
    )

urlpatterns = [
    # Examples:
     
     url(r'^$',BlogListAPIView.as_view(), name='home'),
     url(r'^create/$',BlogCreateAPIView.as_view(), name='create'),
     url(r'^(?P<slug>[\w-]+)/$',BlogDetailAPIView.as_view(), name='detail'),
     url(r'^(?P<slug>[\w-]+)/edit$',BlogUpdateAPIView.as_view(), name='update'),
     url(r'^(?P<slug>[\w-]+)/delete$',BlogDeleteAPIView.as_view(), name='delete'),
     
]

