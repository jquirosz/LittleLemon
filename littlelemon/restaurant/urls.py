from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),

    path('menu/', views.MenuViewSet.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

    path('booking/', views.BookingViewSet.as_view()),
    path('booking/<int:pk>', views.SingleBookingItemView.as_view()),

    path('api-token-auth/', obtain_auth_token),
]
