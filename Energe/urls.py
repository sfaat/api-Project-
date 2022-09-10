from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Auth.views import *
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="Incomet API",
      default_version='v1',
      description="Demo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@enorvision.com"),
      license=openapi.License(name="Enorvision License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('user/', include('Auth.urls')),
    path('api/v1/post/', include('Posts.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('management/', include('management.urls'), name='management'),
    path('', include('IncometAPI.urls'), name='IncometAPI'),
    # path('api/accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    # path('post/', include('Posts.urls')),
]
# admin.site.site_header = 'Admin Dashboard'
# admin.site.site_title = 'Admin'
# admin.site.site_url = 'http://incomet.com/'
# admin.site.index_title = 'Administration'
# admin.empty_value_display = '**Empty**'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
