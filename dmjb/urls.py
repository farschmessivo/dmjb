from django.urls import path
from django.conf.urls import include, url
from dmjb import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_job/$', views.add_job, name='add_job'),
    url(r'^job/(?P<job_slug>[\w\-]+)/$',
        views.show_job, name='show_job'),
]
