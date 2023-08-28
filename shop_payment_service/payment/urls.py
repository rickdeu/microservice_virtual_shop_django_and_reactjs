
from django.urls import path
from payment import views

urlpatterns = [
    #path(f'{views.PayPalPaymentServiceAPI.name}/paypal', views.PayPalPaymentServiceAPI.as_view(), name=views.PayPalPaymentServiceAPI.name),
    #path(f'{views.PaymentOrderDetail.name}/paypal/<str:pk>', views.PaymentOrderDetail.as_view(), name='payment-detail'),
    
    path(f'{views.PaymentOrderCreate.name}/<int:pk>/token=<str:token>', views.PaymentOrderCreate.as_view(), name=views.PaymentOrderCreate.name),



]
