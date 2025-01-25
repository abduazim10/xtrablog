from django.contrib import admin
from .models import Blog, BlogImage, Category, Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogImage)
admin.site.register(Category)
admin.site.register(Comment)