from django.urls import path
from .views import RegisterView, LoginView, AuthenthicationView, ProfileEditView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('authenthication/', AuthenthicationView.as_view(), name='authenthication'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]