from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from prefik import views
from prefik.views import *
from django.urls import path

app_name = 'prefik'
urlpatterns=[
		path('base', Blogshow.as_view()),
		path('',views.index, name='index'),
	]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)