from django.contrib import admin
from .models import Bookmark, Category


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'category', 'published', 'user')
  list_display_links = ('id', 'title')


admin.site.register(Category)

