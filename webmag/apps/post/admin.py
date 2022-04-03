from django.contrib import admin

from ..post.models import PostTag, Post, PostCategory, PostComment


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass

