from django.contrib import admin
from raports.models import Raport


class RaportAdmin(admin.ModelAdmin):
    list_display = ('id','name','schedule','delivery_status')
    list_display_links = ('id','name')
    search_fields = ('id','name','schedule','delivery_status')

admin.site.register(Raport,RaportAdmin)
