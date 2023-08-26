from django.urls import  path 
from . import views
urlpatterns = [
    path('ship', views.ship , name='ship'),
    path('', views.ships , name='ships'),
]