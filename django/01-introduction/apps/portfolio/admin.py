from django.contrib import admin

from portfolio.models import Project, Client, Media, Image

class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['name', 'active',]
    list_filter = ['active',]
    
    date_hierarchy = 'date'
    inlines = [ImageInline, ]
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Client)
admin.site.register(Media)
admin.site.register(Image)
