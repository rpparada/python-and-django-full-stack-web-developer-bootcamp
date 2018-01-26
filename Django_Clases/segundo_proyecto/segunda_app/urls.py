from django.conf.urls import url
from segunda_app import views

urlpatterns = [
    url(r'^$',views.helper,name='help'),
    url(r'^$',views.index,name='index'),
]
