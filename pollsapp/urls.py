from django.urls import path
from .views import *

app_name= 'pollsapp'

urlpatterns = [
    path('',index,name='index'),
    path('vote',vote,name='vote'),
    path('resualt',resualt,name='result')
]
