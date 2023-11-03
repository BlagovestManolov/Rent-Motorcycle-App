from django.urls import path
from motorcycle.tour import views

urlpatterns = [
    path('', views.TourView.as_view(), name='tour-page'),
    path('<int:pk>/', views.SpecTourView.as_view(), name='spec-tour-page'),
]