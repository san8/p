from django.conf.urls.defaults import patterns, url
from clickmuncher import views

urlpatterns = patterns("",
    url(r'^clicks/$', views.count, name="clickmuncher-count"),
)
