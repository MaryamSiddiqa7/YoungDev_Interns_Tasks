from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:product_id>/', views.place_order, name='place_order'),
]
