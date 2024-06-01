from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    
  
    
]
#Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTQwYzcwNTY5ZjNjNmQ3MzNjYjk4YmU1IiwiYXBwbGljYXRpb25faWQiOiI1M2ViYThlOWFjOWMxM2ExMGNiZGQwMzUiLCJpYXQiOjE2ODQxOTgyNzV9.KUNorUvgReXlu-Zy2aAE587f7S9Iv4aGy8aCzaE5HD4