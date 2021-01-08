from django.urls import path
from accounts.api.views import CurrentAccountAPIView

urlpatterns = [
    # Return the current account information
    path('user/', CurrentAccountAPIView.as_view(), name='current-account'),
]