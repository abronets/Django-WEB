from .views import *
from django.conf.urls import url


urlpatterns = [
    url(r'^$', IndexListView.as_view(), name='posts_list'),
    url(r'^create/$', PostCreateView.as_view(), name='post_create'),
    url(r'^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='post_delete'),
    url(r'^create/comment/(?P<pk>\d+)/$', CommentCreateView.as_view(), name='comment_create'),
]

