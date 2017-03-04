from django.conf.urls import include, url


urlpatterns = [
    # Examples:
     
     url(r'^home/','newsletter.views.home', name='home'),
     url(r'^contact/','newsletter.views.contact', name='contact'),
     url(r'^about/','newsletter.views.about', name='about'),
     url(r'^index/','newsletter.views.index',name='index'),
     url(r'^aboutus/','newsletter.views.aboutus',name='aboutus'),
     url(r'^contactus/','newsletter.views.contactus',name='contactus'),

     # url(r'^blog/', include('blog.urls')),
]

