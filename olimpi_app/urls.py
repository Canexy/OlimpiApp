from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # path('', include('register_par.urls')),
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    # path('wag/', include(wagtail_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls))
]

# Media files en Debug:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)