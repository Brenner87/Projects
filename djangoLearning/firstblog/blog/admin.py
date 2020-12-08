from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fileds=('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy='publish'
    ordering=['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'post', 'created', 'active')
    list_filter=('active', 'created', 'updated')
    search_fields=('name', 'email',)

admin.site.register(Post, PostAdmin)
