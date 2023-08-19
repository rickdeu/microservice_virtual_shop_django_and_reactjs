
from django.urls import path
from payment import views

urlpatterns = [
    path(f'{views.PaymentList.name}', views.PaymentList.as_view(), name=views.PaymentList.name),
    path(f'{views.PaymentDetail.name}/<int:pk>', views.PaymentDetail.as_view(), name=views.PaymentDetail.name),


    path('api', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
