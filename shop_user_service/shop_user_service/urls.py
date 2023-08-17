from django.contrib import admin
from django.urls import path, include
from userAuth import urls as url_user
from rest_framework.documentation import include_docs_urls  # api documentation

API_TITLE = 'SHOP API'  # new
API_DESCRIPTION = 'A Web API Description for SHOP SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(url_user)),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

]
