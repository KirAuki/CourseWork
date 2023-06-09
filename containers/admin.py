from django.contrib import admin
from containers.models import Container

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','schedule', 'date')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule', 'date')

admin.site.register(Container, ContainerAdmin)
