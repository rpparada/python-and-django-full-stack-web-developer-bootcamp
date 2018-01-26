from django.conf.urls import url
from primera_app import views

urlpatterns = [
    url('^$',views.index,name='index'),
]
