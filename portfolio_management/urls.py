from django.urls import path
from .views.holdings import HoldingListView

urlpatterns = [
    path('holdings/<int:pk>/', HoldingListView.as_view(), name='user-detail'),
]