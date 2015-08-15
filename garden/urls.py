# -*- coding: utf-8 -*-
# garden/urls.py
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the GardenListView
    url(
        regex=r'^$',
        view=views.GardenListView.as_view(),
        name='list'
    ),

    # URL pattern for the GardenDetailView
    url(
        regex=r'^(?P<title>[\w.@+-]+)/$',
        view=views.GardenDetailView.as_view(),
        name='detail'
    ),
]
