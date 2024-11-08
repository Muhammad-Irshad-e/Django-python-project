from . import views
from django.urls import path
from django.contrib.auth.views import LoginView 

urlpatterns = [
    path('', views.index),
    path('Login',LoginView.as_view(template_name='login.html'),name='login'),
    path('about/', views.about_disp,name='about'),
    path('news/', views.news_disp,name='news'),
    path('contact/', views.contact_disp,name='contact'), 
    path('register/', views.register_disp,name='register'), 

    path('cycle/', views.cycle_disp,name='cycle'), 
]