from django.contrib import admin

from ports.models import DeparturePort,ArrivalPort 


class PortAdmin(admin.ModelAdmin):
    list_display = ('id','name','country', 'city')
    list_display_links = ('id','name')
    search_fields = ('id','name','country', 'city')

admin.site.register(DeparturePort,PortAdmin)
admin.site.register(ArrivalPort,PortAdmin)
