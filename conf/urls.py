from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # path("api/v1/auth-base/", include("rest_framework.urls")),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth_token/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
