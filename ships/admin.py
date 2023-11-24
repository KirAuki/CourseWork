from django.contrib import admin

from ships.models import Ship

class ShipAdmin(admin.ModelAdmin):
    list_display = ('id','name','capacity', 'status')
    list_display_links = ('id','name')
    search_fields = ('id','name','capacity', 'status')
admin.site.register(Ship,ShipAdmin)
