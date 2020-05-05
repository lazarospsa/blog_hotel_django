from django.contrib import admin
from django.contrib.auth.models import Group
from hotel.models import Room, Booking
# Register your models here.
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay

admin.site.site_header = 'Admin Controller'

class RoomAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    list_filter = ('price', 'is_reserved', 'roomtypes')
    list_editable = ['price']
    change_list_template = 'admin/hotel/rooms_change_list.html'

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'room_id', 'date_posted')
    list_filter = ('customer', 'room_id')
    ordering = ("-date_posted",)
    save_as = True
    save_on_top = True
    change_list_template = 'admin/hotel/bookings_change_list.html'


admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.unregister(Group)