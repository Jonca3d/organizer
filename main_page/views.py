from django.shortcuts import render, redirect
# from .models import Main_page
from django.views.generic.base import View


def main_page(request):
    return render(request, 'base_test.html')

