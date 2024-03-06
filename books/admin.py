from django.contrib import admin
from .models import Books

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ('title' , 'subtitle')
    list_filter = ['author']