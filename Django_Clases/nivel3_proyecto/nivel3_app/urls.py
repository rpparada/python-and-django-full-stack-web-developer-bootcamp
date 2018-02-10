from django.conf.urls import url
from nivel3_app import views

urlpatterns = [
    url(r'^$',views.usuarios,name='usuarios'),
    url(r'^$',views.titulos,name='titulos'),
    url(r'^$',views.index,name='index'),

]
