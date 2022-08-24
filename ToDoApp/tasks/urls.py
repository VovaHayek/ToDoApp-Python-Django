from django.urls import path

from . import views

urlpatterns = [
    path('', views.to_do_tasks),
    path('loginForm/', views.loginForm)
]