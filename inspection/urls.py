from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('checkoff', views.checkoff, name="checkoff"),
    path('api', views.api, name="api"),
    path('reports', views.reports, name="reports"),
    path('delete/<reports_id>',views.delete, name= 'delete'),
    path('edit/<reports_id>', views.edit, name= 'edit'),
    path('runreports', views.runreports, name="runreports"),

    
]
#Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQwYzcwNTY5ZjNjNmQ3MzNjYjk4YmU1IiwiYXBwbGljYXRpb25faWQiOiI1M2ViYThlOWFjOWMxM2ExMGNiZGQwMzUiLCJpYXQiOjE2ODQxOTgyNzV9.KUNorUvgReXlu-Zy2aAE587f7S9Iv4aGy8aCzaE5HD4