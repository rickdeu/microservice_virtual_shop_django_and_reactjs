from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# import apps url
from shop import urls as shop_url

from rest_framework.documentation import include_docs_urls #api documentation

API_TITLE = 'DRONES API' # new
API_DESCRIPTION = 'A WEB API FOR DRONES.'



urlpatterns = [
    path('', include(shop_url)),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
