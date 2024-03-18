from django.urls import path
from . import views as drones_views
from django.contrib.auth import views

urlpatterns = [
    path('', drones_views.home_view, name='home_view'),
    path('login/', views.LoginView.as_view(template_name='drones/login.html'), name='login_view'),
    path('logout/', views.LogoutView.as_view(template_name='drones/home.html'), name='logout'),
    path('register/', drones_views.register_view, name='register_view'),
    path('drone-list/', drones_views.drone_list, name='drone_list'),
    path('add-drone/', drones_views.add_drone, name='add_drone'),
    path('drone-list/delete-drone/<int:drone_id>', drones_views.delete_drone, name='delete_drone'),
]
