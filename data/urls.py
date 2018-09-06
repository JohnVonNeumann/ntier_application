from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_data', views.insert_data, name='insert_data'),
    path('select_data', views.select_data, name='select_data'),
]
