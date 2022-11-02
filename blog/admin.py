from django.contrib import admin

from .models import Post, Author, Tag, Comments


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date',)
    list_display = ('title', 'date', 'author',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    # list_filter = 'post'
    # list_editable = "comment"
    # post_title = Post.objects.all().Comments.post_id

    list_display = ("user_name","comment", "post")


# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)
