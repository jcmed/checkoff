from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('checkoff', views.checkoff, name="checkoff"),
    path('api', views.api, name="api"),
    path('reports', views.reports, name="reports"),
    path('delete/<reports_id>',views.delete, name= 'delete'),
    path('edit/<reports_id>', views.edit, name= 'edit'),

    
]