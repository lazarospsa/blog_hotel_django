from django.contrib import admin
from django.contrib.auth.models import Group
from hotel.models import Room
# Register your models here.

admin.site.site_header = 'Admin Controller'

class RoomAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    list_filter = ('price', 'is_reserved', 'roomtypes')
    change_list_template = 'admin/hotel/rooms_change_list.html'

admin.site.register(Room, RoomAdmin)
admin.site.unregister(Group)