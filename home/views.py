from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Nascimento
from django.http import HttpResponse
from django.views import View
# Create your views here.
class NascimentoListView(ListView):

    model = Nascimento
    
"""
class ShowImg(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, World!')
"""