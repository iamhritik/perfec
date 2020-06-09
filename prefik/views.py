from django.shortcuts import render
from django.conf import settings

def index(request):
	context = 'Hello Prefik'
	return render(request, 'index.html', {'test': context})

# Create your views here.
