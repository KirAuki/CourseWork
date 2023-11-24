from django.contrib import admin
from containers.models import Container
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ConteinerResource(resources.ModelResource):

    class Meta:
        model = Container

class ContainerAdmin(ImportExportModelAdmin):
    list_display = ('id','name','schedule', 'date', 'done')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule__name', 'date', 'done')
    list_filter = ['date','done']
    raw_id_fields = ['schedule']
    readonly_fields = ['date']
    date_hierarchy = 'date'
    resources_classes = [ConteinerResource]

    def schedule_short(self, obj):
        return obj.schedule.name

    schedule_short.short_description = 'Расписание'
admin.site.register(Container, ContainerAdmin)

