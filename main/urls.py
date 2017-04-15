from django.conf.urls import url
from main import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from svitla import settings

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^info/$', views.info, name='info'),
        url(r'^about/$', views.about, name='about'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^FAQ/$', views.faq, name='faq'),
        url(r'^price/$', views.price, name='price'),
        url(r'^add_recall/$', views.add_recall, name='add_reall'),
        url(r'^price-wedding/$', views.price_wedding, name='price-wedding'),
        url(r'^price-portret/$', views.price_portret, name='price-portret'),
        url(r'^categories/(?P<type_foto>[\w\-]+)/$', views.categories, name='categories'),
        url(r'^categories/([\w\-]+)/(?P<album_id>[0-9]+)/$', views.albums, name='album')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
