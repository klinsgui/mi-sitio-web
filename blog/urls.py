from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',views.listar_publicaciones),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicacion),
    url(r'^post/new/$', views.nueva_publicacion, name='nueva_publicacion'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_publi, name='editar_publi'),
]
