from django.urls import path
from . import views

urlpatterns = [
    path('', views.memberstitle, name='memberstitle'),
    path('members/', views.members, name='members'),
]