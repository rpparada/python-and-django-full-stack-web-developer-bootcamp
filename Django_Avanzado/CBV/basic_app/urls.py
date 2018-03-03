from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.ColegioLista.as_view(),name='list'),
    # url(r'^(?P<pk>[-\w]+)/$',views.ColegioDetalle.as_view(),name='details'),
    url(r'^(?P<pk>\d+)/$',views.ColegioDetalle.as_view(),name='details'),
    url(r'^create/$',views.ColegioCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.ColegioUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ColegioDeleteView.as_view(),name='delete '),
]
