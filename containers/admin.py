from django.contrib import admin
from containers.models import Container

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','schedule', 'date', 'done')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule__name', 'date', 'done')
    list_filter = ['date','done']
    raw_id_fields = ['schedule']
    readonly_fields = ['date']
    date_hierarchy = 'date'

    def schedule_short(self, obj):
        return obj.schedule.name

    schedule_short.short_description = 'Расписание'
admin.site.register(Container, ContainerAdmin)