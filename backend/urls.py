from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ... your other urlpatterns ...
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


schema_view = get_schema_view(
   openapi.Info(
      title="My showcase Django React.js Celery app for recruitment",
      default_version='v1',
      description="",
      terms_of_service="",
      contact=openapi.Contact(email="contact@yourapp.net"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # replace 'your_app.urls' with your actual app's URL configuration

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]