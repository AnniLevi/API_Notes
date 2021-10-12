from django.urls import path
from .views import index, list_view

urlpatterns = [
    path('', index, name='index'),
    path('list/', list_view, name='list'),
]
