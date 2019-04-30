from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmailList.as_view()),
    path('<int:pk>/', views.EmailDetail.as_view()),
]