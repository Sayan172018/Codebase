from django.conf.urls import url
from django.urls import path
from newapp import views

urlpatterns=[
path('',views.help,name='help'),
path('',views.index,name='index'),
]
