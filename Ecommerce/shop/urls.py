from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shopIndex"),
    path('about', views.about, name="shopAbout")
]
