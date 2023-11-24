from django.contrib import admin

from schedules.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','route','ships_names','departure_date','arrival_date')
    list_display_links = ('id','route')
    search_fields = ('id','route__name','ship__name','departure_date','arrival_date')
    list_filter = ['departure_date','arrival_date']
    filter_horizontal = ['ship']
    date_hierarchy = 'departure_date'
admin.site.register(Schedule,ScheduleAdmin)


    