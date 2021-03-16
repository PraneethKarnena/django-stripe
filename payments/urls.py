from django.urls import path

from payments import views


urlpatterns = [
    path('', views.home)
]