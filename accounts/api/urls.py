from django.urls import path
from accounts.api import views

urlpatterns = [
    # Return the current account information
    path('user/', views.CurrentAccountAPIView.as_view(), name='current-account'),

    path('profiles/', views.ListCreateProfileView.as_view(), name='profile-list'),

    path('profile/', views.RestrieveProfileView.as_view(), name='profile-detail'),

    path('profile/change/<int:pk>/', views.SwitchProfile, name='change-profile'),
]

