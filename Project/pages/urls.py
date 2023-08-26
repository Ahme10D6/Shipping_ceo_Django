from django.urls import  path 
from . import views
urlpatterns = [
    path('', views.Index , name='Index'),
    path('Shipping', views.Shipping , name='Shipping'),
    path('Tracking', views.Tracking , name='Tracking'),
    path('Support', views.Support , name='Support'),
    path('signIn', views.signIn, name='signIn'),
    path('SignUp', views.SignUp , name='SignUp'),
    path('SignUpB', views.SignUpB , name='SignUpB'),
    path('About', views.About , name='About'),
]