from django.contrib import admin
from .models import *

# To use inlineformset in admin site
# You can use either StackedInline or TabularInline as you like

class FileInline(admin.StackedInline):
    model = File
    extra = 3

# class FileInline(admin.TabularInline):
#     model = File
#     extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline]


admin.site.register(Post, PostAdmin)
admin.site.register(File) 
