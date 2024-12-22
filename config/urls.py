from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('engage/admin/', admin.site.urls),
    path('locations/api/', include('engage.locations.api.urls')),
    path('service/api/', include('engage.service.api.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
