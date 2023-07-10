from django.urls import path
from .views import project_list
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'toluport'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('message/', views.message_view, name='message'),
    # Add more URL patterns as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
