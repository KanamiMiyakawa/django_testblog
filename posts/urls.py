from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts_index'),
    path('<int:post_id>/', views.detail, name='posts_detail')
]
