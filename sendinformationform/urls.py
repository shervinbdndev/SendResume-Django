from django.contrib import admin
from django.conf import settings
from django.urls.conf import (path , include)
from django.conf.urls.static import static

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='' , view=include('sendresume.urls'))
]

if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)