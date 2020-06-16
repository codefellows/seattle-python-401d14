from django.urls import path
from .views import HomePageView, SnacksView, SnackDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snacks/', SnacksView.as_view(), name='snacks'),
    path('snack/<int:pk>', SnackDetailsView.as_view(), name='snack_details')
]
