from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('engage/admin/', admin.site.urls),
    path('api/locations/', include('engage.locations.api.urls')),
]
