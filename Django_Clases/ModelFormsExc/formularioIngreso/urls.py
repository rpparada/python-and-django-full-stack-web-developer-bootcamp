from django.conf.urls import url
from formularioIngreso import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^$',views.index,name='listaUsuario')
]
