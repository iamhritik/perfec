from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import re_path
from prefik import views
from prefik.views import *
from django.urls import path

app_name = 'prefik'
urlpatterns=[
		path('',views.index, name='index'),
		path('blogs',views.blogs, name='blogs'),
		path('blogs/<slug>/', views.show, name='show'),
	]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)