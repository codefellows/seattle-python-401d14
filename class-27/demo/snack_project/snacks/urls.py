from django.urls import path
from .views import HomePageView, SnacksPageView, SnackDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snacks/', SnacksPageView.as_view(), name='snacks'),
    path('snack_details/<int:pk>', SnackDetailsView.as_view(), name='snack_details'),
]
