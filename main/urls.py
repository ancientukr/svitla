from django.conf.urls import url
from main import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from svitla import settings

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^info/$', views.info, name='info'),
        url(r'^about/$', views.about),
        url(r'^contact/$', views.contact),
        url(r'^FAQ/$', views.faq),
        url(r'^price/$', views.price),
        url(r'^add_recall/$', views.add_recall),
        url(r'^price-wedding/$', views.price_wedding),
        url(r'^price-portret/$', views.price_portret),
        url(r'^categories/(?P<type_foto>[\w\-]+)/$', views.categories),
        url(r'^categories/([\w\-]+)/(?P<album_id>[0-9]+)/$', views.albums)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
