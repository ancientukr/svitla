from django.conf.urls import patterns, url, include
from main import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^main/', include('main.urls')),
]
