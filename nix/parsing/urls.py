from django.conf.urls import url

from parsing.views import *

urlpatterns = [
    url(r'^api/posts/$', PostList.as_view(), name='posts-list'),
    url(r'^api/posts/(?P<site>.*)/$', PostList.as_view(), name='posts-site-list'),

]
