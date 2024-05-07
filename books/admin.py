from django.contrib import admin
from .models import Category,Subcategory,Book,Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Comment)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    

admin.site.register(Book, BookAdmin)