from django.conf.urls import url
from django.urls import path
from djangtwoapp import views

urlpatterns=[
# path('',views.index,name='index'),
path('',views.user,name='user'),
path('',views.index,name='index'),
]
