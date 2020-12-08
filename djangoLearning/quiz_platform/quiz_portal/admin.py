from django.contrib import admin
from quiz_portal.models import quiz
# Register your models here.

class quizAdmin(admin.ModelAdmin):
    list_display=['id','title', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fileds=['title', 'description']
    raw_id_fields = ['author',]
    date_hierarchy='publish'
    ordering=['status', 'publish']



admin.site.register(quiz, quizAdmin)

