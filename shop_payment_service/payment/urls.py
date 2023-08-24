
from django.urls import path
from payment import views

urlpatterns = [
    path(f'{views.PayPalPaymentServiceAPI.name}/paypal', views.PayPalPaymentServiceAPI.as_view(), name=views.PayPalPaymentServiceAPI.name),
    path(f'{views.PayPalPaymentServiceAPI.name}/paypal/<str:pk>', views.PayPalPaymentServiceAPI.as_view(), name='payment-detail'),


    path('api', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
