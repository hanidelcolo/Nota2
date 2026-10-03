from django.contrib import admin
from .models import News
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'category', 'reading_status', 'is_favorite', 'rating', 'created')
    list_editable = ('reading_status', 'is_favorite')
    list_filter = ('reading_status', 'is_favorite', 'category')
    search_fields = ('title', 'author', 'category')
admin.site.register(News, ProjectAdmin)
# Register your models here.
