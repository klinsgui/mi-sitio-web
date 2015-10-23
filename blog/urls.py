from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$',views.listar_publicaciones),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicacion),
    url(r'^post/new/$', views.nueva_publicacion, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_publicacion, name='post_edit'),
]
