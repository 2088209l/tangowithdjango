from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns ('',
    url(r'^$', views.index, name = 'index'),
    url(r'^about', views.about, name = 'about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)  #pass the value of category_name_url to the category() function
