from django.urls import path
from firstapp import views


#urls here
urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
]
