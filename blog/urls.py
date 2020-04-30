from django.urls import path
from blog import views
from blog.views import UserPostListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView #egw ta eftia3a auta sto views.py


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #apo views.home to alla3a se PostListView.as_view()
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), #apo views.home to alla3a se PostListView.as_view()
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), #grab the value from link id of post me to <pk> epeidh 3erw oti einai integer vazw <int:pk>
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]