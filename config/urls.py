
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('payment/', include('apps.payment.urls')),
    path('courses/', include('apps.courses.urls')),
    path('marketplace/', include('apps.marketplace.urls')),
    
    # API URLs
    path('api/payment/', include('apps.payment.api.urls')),
    path('api/courses/', include('apps.courses.api.urls')),
    path('api/marketplace/', include('apps.marketplace.api.urls')),
]

from django.conf import settings
from django.conf.urls import include
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

