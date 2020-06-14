from django.contrib import admin
from prefik.models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class ChoiceAdmin(admin.ModelAdmin):
    pass
