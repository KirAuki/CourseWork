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
    item_size = fields.Field(column_name='Размеры контейнера', attribute='size')
    item_weight = fields.Field(column_name='Вес контейнера', attribute='weight')
    item_date = fields.Field(column_name='Дата принятия', attribute='date', widget=DateWidget(format='%Y-%m-%d'))
    item_done = fields.Field(column_name='Доставлено', attribute='done', widget=CustomBooleanWidget())
    
    def dehydrate_item_weight(self, container):
        return f'{container.weight} kg'

    
    
    def get_export_headers(self):
        headers = []
        for field in self.get_fields():
            model_fields = self.Meta.model._meta.get_fields()
            header = next((x.verbose_name for x in model_fields if x.name == field.column_name), field.column_name)
            headers.append(header)
        return headers

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
        queryset = super().get_export_queryset(request)
        return queryset.filter(done=True)


admin.site.register(Container, ContainerAdmin)

