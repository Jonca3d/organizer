from django.shortcuts import render, redirect
from .models import Bookmark
from django.views.generic.base import View
from .forms import BookmarkForm

def bookmarks_page(request):
    return render(
        request,
        'bookmarks/index.html',
        {'bookmarks': Bookmark.objects.all()})


class AddBookmark(View):
    def post(self, request):
        form = BookmarkForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("/")
