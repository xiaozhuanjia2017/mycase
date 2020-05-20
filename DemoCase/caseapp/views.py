from django.shortcuts import render
from django.views import View
from .models import *


class IndexView(View):

    def get(self, request):
        queryset = Case.objects.all()
        return render(request, "index.html", {"data": queryset})
