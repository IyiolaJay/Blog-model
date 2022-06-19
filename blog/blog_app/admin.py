from django.contrib import admin

from .models import Blog_user, Post

# Register your models here.
admin.site.register(Blog_user)
admin.site.register(Post)