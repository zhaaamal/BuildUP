# users/urls.py
from django.urls import path
from .views import UserRegistrationView, UserDetailView, LogoutView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
]
