from django.urls import path

from . import views

urlpatterns = [
    path('', views.top, name='pages_top'),
]
