from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path("signup/", views.register, name="register"),
    path('create/', views.create, name='create'),
    path('createtest/', views.createtest, name='createtest'),
    path('updatesurvey/<int:id>', views.updatesurvey, name='updatesurvey'),
    path('feed/', views.feed, name='feed'),
]