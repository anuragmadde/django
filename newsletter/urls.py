from django.conf.urls import include, url


urlpatterns = [
    # Examples:
     
     url(r'^home/','newsletter.views.home', name='home'),
     url(r'^contact/','newsletter.views.contact', name='contact'),
     url(r'^about/','newsletter.views.about', name='about'),
     # url(r'^blog/', include('blog.urls')),
]

