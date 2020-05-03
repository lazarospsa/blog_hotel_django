from django.urls import path
from hotel import views
from hotel.views import about, home, BookingsListView, thanks, BookCreateView,BookRoomView, RoomSearchView, RoomDetailView, RoomListView, RoomUpdateView, RoomDeleteView, RoomCreateView
#from hotel.views import UserPostListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView #egw ta eftia3a auta sto views.py

urlpatterns = [
    path('', views.home, name='hotel-home'),
    path('rooms/', RoomListView.as_view(), name='hotel-rooms'),
    path('bookingslist/', BookingsListView.as_view(), name='hotel-booking-list'),
    path('about/', views.about, name='hotel-about'),
    path('thanks/', views.thanks, name='hotel-thanks'),
    path('rooms/search/', RoomSearchView.as_view(), name='hotel-room-search'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='hotel-room-detail'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('rooms/<int:pk>/update/', RoomUpdateView.as_view(), name='hotel-room-update'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('rooms/<int:pk>/delete/', RoomDeleteView.as_view(), name='hotel-room-delete'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('rooms/new/', RoomCreateView.as_view(), name='hotel-room-create'),
    path('rooms/book/<int:pk>', BookCreateView.as_view(), name='hotel-room-booking'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    
]