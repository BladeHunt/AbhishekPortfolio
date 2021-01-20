from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Make sure frontend loads before backend
    path('', include('frontend.urls')),
    path('', include('backend.urls')),
    path('tinymce/', include('tinymce.urls')),
]

handler404 = "frontend.views.error_404_view"
