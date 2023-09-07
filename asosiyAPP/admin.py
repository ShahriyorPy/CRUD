from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone']
    list_editable = ['name','phone']
    search_fields = ['name']
    search_help_text = "Ismi, ismi bo'yicha qidiring."
    list_filter = ["name"]
    list_per_page = 5

