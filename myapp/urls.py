from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.HomeView.as_view(), name='candit-detail'),
]
