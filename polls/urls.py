from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(),
        name='results'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),

]
