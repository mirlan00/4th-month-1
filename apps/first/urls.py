from django.urls import path
from apps.first.views import index

urlpatterns = [
    path('',index,name='index')
]
