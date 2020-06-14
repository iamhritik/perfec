from django.shortcuts import render
from django.http import Http404 , HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.conf import settings
from prefik.models import Blog
from prefik.forms import Blogform

def index(request):
	return render(request, 'index.html', {'test1':'testing'})

class Blogshow(View):
	template = 'index.html'
	form_class = Blogform()
	def get(self,request,*args, **kwargs):
		form = self.form_class
		return render(request,self.template,{'form':form})




# Create your views here.
