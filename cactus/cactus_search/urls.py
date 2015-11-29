#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('cactus_search.views',
                       url(r'^search/$', 'search'),
                   )
