from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('view/', views.view, name='view'),
    path('updateItem/', views.update_item, name='updateItem'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]