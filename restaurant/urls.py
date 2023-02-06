from django.urls import path, include
from . import views
from rest_framework.authtoken import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'), 
     path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('api/reservations', views.reservations),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
     path('api-token-auth/', views.obtain_auth_token),
]