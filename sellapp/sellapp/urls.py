from django.conf.urls import patterns, include, url
from django.contrib import admin
from app1.views import seller_form

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sellapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sell/', seller_form),
)
