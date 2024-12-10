from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='seller_dashboard'),
    path("profile/", views.profile_view, name='profile_seller')
]