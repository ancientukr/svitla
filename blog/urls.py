from django.conf.urls import url
from blog import views

urlpatterns = [
        url(r'^$', views.blog, name='blog'),
        url(r'^(?P<post_id>[0-9]+)/$', views.post, name='post')
]