from django.contrib import admin
from containers.models import Container

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','schedule', 'date', 'done')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule', 'date', 'done')
    list_filter = ['date','done']
admin.site.register(Container, ContainerAdmin)
