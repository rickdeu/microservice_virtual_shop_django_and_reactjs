from django.contrib import admin
from django.urls import path, include
from payment import urls as payment_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(payment_urls)),
    path('payments/', include('payments.urls')),
]
