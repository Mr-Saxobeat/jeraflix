"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from accounts.views import CustomLoginView, CustomRegistrationView
from accounts.forms import AccountForm
from movies.views import WatchListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registration via browser
    path('accounts/register/', 
        CustomRegistrationView.as_view(
            form_class=AccountForm,
            success_url='/',
            ),
            name='django_registration_register'),

    path('accounts/login/',
        CustomLoginView
        ),

    # Urls used by django_registration
    path('accounts/', 
        include('django_registration.backends.one_step.urls')), 

    # Login via browser
    path('accounts/', 
        include('django.contrib.auth.urls')),

    path('api/accounts/',
        include('accounts.api.urls')), 

    # Login via browsable API from rest_framework
    path('api-auth/', 
        include('rest_framework.urls')),

    # Login via rest
    path('api/rest-auth/', 
        include('rest_auth.urls')),

    # Registration via rest
    path('api/rest-auth/registration/', 
        include('rest_auth.registration.urls')),

    path('api/movies/',
        include('movies.api.urls')),

    re_path(r'^.*$', IndexTemplateView.as_view(), name='entry-point'),

    path('watchlist/',
        WatchListView, name='profile-watchlist'),
]
