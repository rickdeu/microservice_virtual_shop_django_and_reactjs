from django.contrib import admin
from django.urls import path, include

# import apps url
from shop import urls as shop_url

urlpatterns = [
    path('', include(shop_url)),
    path('admin/', admin.site.urls),

]

