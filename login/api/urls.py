from django.conf.urls import include, url
from .views import (
    UserCreateAPIview,
    UserLoginAPIView,
    )

urlpatterns = [
    # Examples:
     
     url(r'^register/$',UserCreateAPIview.as_view(), name='register'),
     url(r'^login/$',UserLoginAPIView.as_view(), name='login'),
     
]

