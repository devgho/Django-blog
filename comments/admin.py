from django.contrib import admin
from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','url','content','post']


admin.site.register(Comment,CommentAdmin)