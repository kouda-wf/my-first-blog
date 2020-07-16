from django.urls import path
from . import views
rlpatterns = [
    path('', views.post_list, name='post_list'),
]