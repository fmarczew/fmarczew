from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'landing/index.html')