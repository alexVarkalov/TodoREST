from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


from .views import TaskViewSet, UserViewSet, api_root
from rest_framework import renderers

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^task/$', task_list, name='task-list'),
    url(r'^task/(?P<pk>[0-9]+)/$', task_detail, name='task-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])