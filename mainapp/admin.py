from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'preambule', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk', )
    list_per_page = 3
    search_fields = ('title', 'preambule', 'text')
    date_hierarchy = ('created_at')

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


admin.site.site_title = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.site_header = 'Костромская Федерация Тхэквондо-ИТФ'
