from django.urls import path
from .views import  LoginView, RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView,TokenBlacklistView
 
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('profile/',UserProfileView.as_view(),name='user_profile'),
    path('logout/',TokenBlacklistView.as_view(),name='logout')
]

