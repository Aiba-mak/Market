
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include('goods.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.PRODUCTS_URL, document_root=settings.PRODUCTS_ROOT)