from django.conf.urls import url
from django.urls import path
from modelformapp import views

urlpatterns=[
path('',views.index,name='index'),
path('',views.users,name='users'),
]
