"""Book models admin."""

# Django
from django.contrib import admin

#django import export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Models
from apps.books.models import Book


class BookResource(resources.ModelResource):
    class Meta:
        model = Book



class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Book, BookAdmin)