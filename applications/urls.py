from django.conf.urls import url
from django.urls import path
from applications import views as views_app

urlpatterns = [
    path('esyd/', views_app.esydApp, name='esyd'),
]