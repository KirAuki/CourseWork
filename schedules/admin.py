from django.contrib import admin

from schedules.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','name','ship','route', 'departure_date','arrival_date')
    list_display_links = ('id','name')
    search_fields = ('id','name','ship','route', 'departure_date','arrival_date')

admin.site.register(Schedule,ScheduleAdmin)
