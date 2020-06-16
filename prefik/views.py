from django.shortcuts import render, get_object_or_404
from django.http import Http404 , HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.conf import settings
from prefik.models import Blog
from prefik.forms import Blogform

def index(request):
	blogs = Blog.objects.all()[:3]
	return render(request, 'index.html',{'blogs':blogs})

def blogs(request):
	blogs  = Blog.objects.all()
	return render(request, 'blogs.html' ,{'blogs':blogs})

def show(request, slug):
	unslug = slug.replace('-', ' ') 
	detail = Blog.objects.get(title=unslug)
	return render(request, 'show.html',{'detail':detail})





# Create your views here.
