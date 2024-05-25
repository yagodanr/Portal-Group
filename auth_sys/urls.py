from django.urls import path
from .views import CustomLoginView, CustomRegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login-form'),
    path('register/', CustomRegistrationView.as_view(), name='register')
    
]
