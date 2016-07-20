from django.conf.urls import include, url
from .views import (
    login_view,
    register_view,
    logout_view,
    )

urlpatterns = [
    # Examples:
     
     url(r'^login/$',login_view,name='login'),
     url(r'^register/$',register_view, name='register'),
     url(r'^logout/$',logout_view, name='logout'),
     
     
]
