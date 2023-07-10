from django.urls import path
from .views import project_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'toluport'

urlpatterns = [
    path('', project_list, name='project_list'),
    # Add more URL patterns as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
