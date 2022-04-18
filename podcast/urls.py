from django.contrib import admin
from django.urls import path
from . import views
app_name = 'podcast'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload_show', views.uploadShow, name="upload_show"),
]
