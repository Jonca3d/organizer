from django.shortcuts import render, redirect
from .models import Bookmark, Category
from django.views.generic.base import View
from .forms import BookmarkForm


def main_page(request):
    return render(request, 'base.html')

def test_page(request):
    return render(request, 'base_test.html')


def bookmarks_page(request):
    return render(
        request,
        'bookmarks/index.html',
        {'bookmarks': Bookmark.objects.all(), 'categories': Category.objects.all()})


class AddBookmark(View):
    def post(self, request):
        form = BookmarkForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect("bookmark")
