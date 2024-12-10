from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('literasi/', views.literasi_view, name='literasi'),
    path('pembeli/pemasaran/', views.pemasaran_view, name="pemasaran"),
    path('about/', views.about_view, name='about'),
    path('cart/', views.cart_view, name='cart'),  

]