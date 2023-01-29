from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.start_page),
    path('places/<int:place_id>/', views.detail_place, name='places'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
