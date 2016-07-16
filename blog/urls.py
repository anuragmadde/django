from django.conf.urls import include, url
from .views import (
    blog_home,
    blog_create,
    blog_detail,
    blog_update,
    blog_delete,
    )

urlpatterns = [
    # Examples:
     
     url(r'^$',blog_home, name='home'),
     url(r'^create/$',blog_create, name='create'),
     url(r'^(?P<slug>[\w-]+)/$',blog_detail, name='detail'),
     url(r'^(?P<slug>[\w-]+)/edit$',blog_update, name='update'),
     url(r'^(?P<slug>[\w-]+)/delete$',blog_delete, name='delete'),
     
]

