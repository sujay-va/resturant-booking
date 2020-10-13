from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPage, name='user_page'),
    path('admindash/', views.dash, name='dash'),

    path('admindash/show_cust', views.show_cust, name='show_cust'),
    path('admindash/show_rest', views.show_rest, name='show_rest'),
    path('admindash/show_torder', views.show_torder, name='show_torder'),
    path('admindash/show_porder', views.show_porder, name='show_porder'),

    path('admindash/add_cust', views.add_cust, name='add_cust'),
    path('admindash/add_rest', views.add_rest, name='add_rest'),
    path('admindash/add_torder', views.add_torder, name='add_torder'),
    path('admindash/add_porder', views.add_porder, name='add_porder'),

    path('admindash/show_cust/<str:pk>', views.view_cust, name='view_cust'),
    path('admindash/show_rest/<str:pk>', views.view_rest, name='view_rest'),
    path('admindash/view_torder', views.view_torder, name='view_torder'),
    path('admindash/view_porder', views.view_porder, name='view_porder'),




    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.register, name='register'),

]
