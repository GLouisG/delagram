from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models.base import ObjectDoesNotExist
# Create your views here.
def landing(request):
  pics = "Will be something soon"
  return render(request, 'index.html', {"pics": pics})
