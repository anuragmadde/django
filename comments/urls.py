from django.conf.urls import include, url
from .views import (
    comment_detail
    )

urlpatterns = [
    # Examples:
     
     url(r'^(?P<id>\d+)/$',comment_detail, name='detail'),
     # url(r'^(?P<slug>[\w-]+)/delete$',blog_delete, name='delete'),
     
]

