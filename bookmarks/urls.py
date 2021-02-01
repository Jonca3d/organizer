from django.urls import path
from . import views


urlpatterns = [
  path('', views.bookmarks_page),
  path('addbookmark', views.AddBookmark.as_view(), name='add_bookmark' )
]
