from django.conf.urls import url
from modelos_aplicacion import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
