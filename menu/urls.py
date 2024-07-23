from django.urls import path
from . import views
from .views import example_view

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<str:menu_name>/', example_view, name='example_view'),
]