# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 10 15:38
# Author Yo
# Email YoLoveLife@outlook.com
from django.conf.urls import url
from ..views import script,playbook
urlpatterns = [
    #Resource script url
    url(r'^script/$', script.OperationScriptListView.as_view(), name='script'),
    url(r'^script/(?P<pk>[0-9]+)/update/',script.OperationScriptUpdateView.as_view(),name='scriptupdate'),
    url(r'^script/(?P<pk>[0-9]+)/detail/', script.OperationScriptDetailView.as_view(), name='scriptdetail'),

    #Resource playbook url
    url(r'^playbook/$',playbook.OperationPlaybookListView.as_view(),name='playbook'),
    url(r'^playbook/(?P<pk>[0-9]+)/update/', playbook.OperationPlaybookUpdateView.as_view(), name='playbookupdate'),

    #Resource adhoc url
    url(r'^adhoc/(?P<pk>[0-9]+)/editor/',playbook.OperationAdhocEditorView.as_view(),name='adhoceditor'),
    # url(r'^script/(?P<pk>[0-9]+)/detail/', script.OperationPlaybookDetailView.as_view(), name='playbookdetail'),
]