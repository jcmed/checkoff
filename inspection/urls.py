from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('fetch_api_data/',views.fetch_api_data, name='fetch_api_data'),
    path('active/',views.active, name= "active"),
    path('911/',views.active_2, name="911"),
    path('home2', views.home2, name="home2"),
    path('home3', views.home3, name="home3"),
    
]
