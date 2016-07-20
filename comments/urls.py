from django.conf.urls import include, url
from .views import (
    comment_detail,
    comment_delete
    )

urlpatterns = [
    # Examples:
     
     url(r'^(?P<id>\d+)/$',comment_detail, name='detail'),
     url(r'^(?P<id>\d+)/delete/$',comment_delete, name='delete'),
     
     
]

