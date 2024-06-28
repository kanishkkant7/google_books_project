from django.contrib import admin

from .models import Book, Comment, Like, UserCollection

# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserCollection)