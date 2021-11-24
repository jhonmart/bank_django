from django.urls import re_path
from users.views import UserViewSet

# URLConf
urlpatterns = [
    re_path(r'^detail/?$', UserViewSet.as_view({'get': 'show_user'}), name='show_user'),
    re_path(r'^create/?$', UserViewSet.as_view({'post': 'insert_user'}), name='insert_user'),
    re_path(r'^list/?$', UserViewSet.as_view({'get': 'list_users'}), name='list_users'),
    re_path(r'^(?P<user_id>[\d]+)/?$', UserViewSet.as_view({'get': 'get_user'}), name='get_user'),
]