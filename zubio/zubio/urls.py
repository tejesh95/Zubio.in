from django.conf.urls import patterns, include, url
from django.contrib import admin
from users_zubio.views import seller_form,buyer_feed
import allauth.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zubio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sell/', seller_form),
    url(r'buyer_feed/', buyer_feed),
    url(r'^accounts/', include(allauth.urls)),
)