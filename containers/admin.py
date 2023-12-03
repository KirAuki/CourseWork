from django.contrib import admin
from containers.models import Container
from import_export import resources, fields
from import_export.widgets import DateWidget , BooleanWidget
from import_export.admin import ImportExportMixin,ExportActionModelAdmin

class CustomBooleanWidget(BooleanWidget):
    def render(self, value, obj=None):
        return 'Да' if value else 'Нет'
    
class ContainerResource(resources.ModelResource):
    item_name = fields.Field(column_name='Название контейнера', attribute='name')
    item_schedule_name = fields.Field(column_name='Расписание', attribute='schedule__name')
    item_size = fields.Field(column_name='Размер', attribute='size')
    item_weight = fields.Field(column_name='Вес', attribute='weight')
    item_date = fields.Field(column_name='Дата принятия', attribute='date', widget=DateWidget(format='%Y-%m-%d'))
    item_done = fields.Field(column_name='Доставлено', attribute='done', widget=CustomBooleanWidget())
    
    class Meta:
        model = Container
        fields = ('item_name', 'item_schedule_name', 'item_size', 'item_weight', 'item_date', 'item_done')
        export_order = fields

class ContainerAdmin(ImportExportMixin,ExportActionModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','schedule', 'date', 'done')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule__name', 'date', 'done')
    list_filter = ['date','done']
    raw_id_fields = ['schedule']
    readonly_fields = ['date']
    date_hierarchy = 'date'
    resources_classes = [ContainerResource]

    def schedule_short(self, obj):
        return obj.schedule.name

    schedule_short.short_description = 'Расписание'

    resource_class = ContainerResource

    def get_export_queryset(self, request):
        return super().get_export_queryset(request)


admin.site.register(Container, ContainerAdmin)

