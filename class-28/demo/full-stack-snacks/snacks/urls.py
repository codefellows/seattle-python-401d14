from django.urls import path
from .views import SnackCreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView

urlpatterns = [
    path('snacks/new', SnackCreateView.as_view(), name="snack_create"),
    path('snacks/<int:pk>/delete', SnackDeleteView.as_view(), name="snack_delete"),
    path('snacks/<int:pk>/', SnackDetailView.as_view(), name="snack_detail"),
    path('', SnackListView.as_view(), name="snack_list"),
    path('snacks/<int:pk>/edit', SnackUpdateView.as_view(), name="snack_update"),
]
