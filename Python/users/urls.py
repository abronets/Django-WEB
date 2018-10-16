from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from .views import UserDetailView, CustomLoginView, UserRegister

urlpatterns = [
    url(r'detail/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^login/$', CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page='/users/login'), name='logout'),
]