
from django.urls import path
from order import views

urlpatterns = [
    path(f'api/order_create', views.orderCreate, name='order_create'),
    path(f'api/order_detail/<int:pk>', views.order_detail, name='order_detail'),

]
