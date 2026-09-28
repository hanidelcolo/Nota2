from django.contrib import admin
from .models import News
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(News, ProjectAdmin)
# Register your models here.
