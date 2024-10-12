from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('menu/', views.MenuViewSet.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    path('booking/', views.BookingViewSet.as_view()),
    path('booking/<int:pk>', views.SingleBookingItemView.as_view()),
]
