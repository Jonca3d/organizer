from django.urls import path
from . import views


urlpatterns = [
  path('', views.main_page, name='main_page'),
  path('bookmark', views.bookmarks_page, name='bookmark'),
  path('addbookmark', views.AddBookmark.as_view(), name='add_bookmark' ),
  path('test_page', views.test_page, name='test_page'),
]
