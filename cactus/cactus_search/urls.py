#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('cactus_search.views',
                       # Vue home
                       #url(r'/$', 'home'),
                       url(r'^home/$', 'home'),
                       url(r'^search/$', 'search'),
                   )
