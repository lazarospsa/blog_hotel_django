from django.urls import path
from hotel import views
from hotel.views import about, home, BookingsListView, thanks, BookCreateView, BookRoomView, RoomSearchView, RoomDetailView, RoomListView, RoomUpdateView, RoomDeleteView, RoomCreateView

urlpatterns = [
    path('', views.home, name='hotel-home'),
    path('rooms/', RoomListView.as_view(), name='hotel-rooms'),
    path('bookingslist/', BookingsListView.as_view(), name='hotel-booking-list'),
    path('about/', views.about, name='hotel-about'),
    path('thanks/', views.thanks, name='hotel-thanks'),
    path('rooms/search/', RoomSearchView.as_view(), name='hotel-room-search'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='hotel-room-detail'),
    path('rooms/<int:pk>/update/', RoomUpdateView.as_view(), name='hotel-room-update'),
    path('rooms/<int:pk>/delete/', RoomDeleteView.as_view(), name='hotel-room-delete'),
    path('rooms/new/', RoomCreateView.as_view(), name='hotel-room-create'),
    path('rooms/book/<int:pk>', BookCreateView.as_view(), name='hotel-room-booking'),
]