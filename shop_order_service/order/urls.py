
from django.urls import path
from order import views

urlpatterns = [
    path(f'{views.OrderCreate.name}', views.OrderCreate.as_view(), name=views.OrderCreate.name),
    #path(f'order_detail/<int:pk>', views.order_detail, name='order_detail'),
    path(f'{views.OrderDetail.name}/<int:pk>/?token=<str:token>', views.OrderDetail.as_view(), name=views.OrderDetail.name),
    path(f'{views.UserOrders.name}/<str:token>', views.UserOrders.as_view(), name=views.UserOrders.name),
    #path(f'get_user_orders/<str:token>', views.get_user_orders, name='get_user_orders'),


    path('api/', views.ApiRoot.as_view(), name=views.ApiRoot.name),


]
