from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [ 
    # Examples:
     url(r'^$', 'login.views.login_view',name='django'),
     url(r'^newsletter/',include('newsletter.urls', namespace='newsletter')),
     url(r'^comments/',include('comments.urls', namespace='comment')),
     url(r'^account/',include('login.urls', namespace='account')),
     url(r'^blog/',include('blog.urls', namespace='blog')),
     # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api/token/auth/', obtain_jwt_token),
    url(r'^api/user/', include('login.api.urls', namespace='api-login')),
    url(r'^api/comments/', include('comments.api.urls', namespace='api-comment')),
    url(r'^api/', include('blog.api.urls', namespace='api')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)