from django.contrib import admin
from django.urls import path, include
from order import urls as order_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(order_urls)),
]
