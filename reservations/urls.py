from . import views
from django.urls import path

urlpatterns = [
    path("", views.BookingList.as_view(), name="home"),
    path('<slug:slug>/', views.BookingDetail.as_view(), name='booking_detail'),
]