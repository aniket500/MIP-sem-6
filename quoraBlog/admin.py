from django.contrib import admin
from .models import Post, Community, Comment

admin.site.register(Post)
admin.site.register(Community)
admin.site.register(Comment)