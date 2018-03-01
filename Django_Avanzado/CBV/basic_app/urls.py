from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.ColegioLista.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.ColegioDetalle.as_view(),name='details'),
]
