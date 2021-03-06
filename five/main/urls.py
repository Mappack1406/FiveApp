from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path("signup/", views.register, name="register"),
    path('create/', views.create, name='create'),
    path('updatesurvey/<int:id>', views.updatesurvey, name='updatesurvey'),
    path('deletesurvey/<int:id>', views.deletesurvey, name='deletesurvey'),
    path('feed/', views.feed, name='feed'),
    path('details/<int:id>/', views.details, name='details'),
]