from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    filter_horizontal = ('tags', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Travel)
admin.site.register(Contact)
admin.site.register(Archives)
admin.site.register(SubPost)
admin.site.register(About)
admin.site.register(Contact1)