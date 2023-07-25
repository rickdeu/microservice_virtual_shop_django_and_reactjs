
from django.urls import path
from shop import views

urlpatterns = [
    path(f'{views.CategoryList.name}/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path(f'{views.CategoryDetail.name}/<int:pk>', views.CategoryDetail.as_view(), name=views.CategoryDetail.name),

    path(f'{views.ProductList.name}/', views.ProductList.as_view(), name=views.ProductList.name),
    path(f'{views.ProductDetail.name}/<int:pk>', views.ProductDetail.as_view(), name=views.ProductDetail.name),




    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

]
