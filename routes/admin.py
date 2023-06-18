from django.contrib import admin

from routes.models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id','name','departure', 'arrival','distance')
    list_display_links = ('id','name','departure','arrival')
    search_fields = ('id','name','departure', 'arrival','distance')
    list_filter = ['departure','arrival','distance']
admin.site.register(Route,RouteAdmin)
