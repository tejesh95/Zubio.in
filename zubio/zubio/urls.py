from django.conf.urls import patterns, include, url
from django.contrib import admin
import gym.urls
import gym.views

from gym.views import ArticleListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zubio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', gym.views.index),
    url(r'^list/', gym.views.gym_listing_form),
    url(r'^login/', gym.views.login),
    url(r'^gymprofile/', gym.views.gym_profile),
    url(r'^index/', gym.views.index),
    url(r'^zubio/locations/', gym.views.api),
    url(r'^upload/', gym.views.upload_form),
    url(r'^trainer/', gym.views.trainer_profile),
    url(r'^search/', gym.views.search_listings),

)

