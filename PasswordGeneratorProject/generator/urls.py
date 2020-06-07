from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('password', views.password, name="password"),
    path('aboutPage', views.about, name="about")
]
