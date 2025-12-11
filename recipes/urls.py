from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_recipes, name='recipes'),  # /recipes/
]
