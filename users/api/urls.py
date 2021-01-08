from django.urls import path
from users.api.views import CurrentUserAPIView

urlpatterns = [
    # Return the current user information
    path('user/', CurrentUserAPIView.as_view(), name='current-user'),
]