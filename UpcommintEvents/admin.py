from django.contrib import admin
from UpcommintEvents.models import UpcommingEvents
class UpcommingEventsAdmin(admin.ModelAdmin):
    list_display = ('Event_name', 'Event_title', 'Event_desc', 'Event_img')
admin.site.register(UpcommingEvents, UpcommingEventsAdmin)
# Register your models here.
