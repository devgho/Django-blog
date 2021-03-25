# usr/bin/python
# -*-coding:utf-8-*-
#from django.conf.urls import url
from django.urls import path,re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:pk>/",views.detail,name="detail"),
    re_path(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archive,name="archive"),
    path("category/<int:ct>",views.category,name="category"),
    path("author/<str:name>",views.author,name="author")
]