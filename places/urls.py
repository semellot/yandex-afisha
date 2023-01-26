from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page),
    path('places/<int:place_id>/', views.detail_place),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
