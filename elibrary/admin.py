from django.contrib import admin

from .models import (
	Author, Publisher, Book, BookCategory, BookEdition, BookItem
	)

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	search_fields = ['last_name', 'first_name']
	ordering = ['last_name', 'first_name']
		
class BookAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title',]


		
admin.site.register (Author, AuthorAdmin)

admin.site.register (Book, BookAdmin)

admin.site.register (Publisher)

admin.site.register (BookCategory)

admin.site.register (BookEdition)
admin.site.register (BookItem)
