from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    path('', views.RoomListCreate.as_view()),
    re_path(r'(?P<pk>[0-9]+)', views.RoomRetrieveUpdateDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)