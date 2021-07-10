import datetime
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.contrib.auth.admin import UserAdmin
from .admin_logic import add_days
from django.db.models import Max
from .models import *


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('finish_time', 'total_price', 'master_id', 'id')
    readonly_fields = ('total_price',)
    raw_id_fields = ('customer',)

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(master_id=Master.objects.get(user=request.user))


class PreOrderAdmin(admin.ModelAdmin):
    list_display = ('reserved_date', 'reserved_time', 'description', 'master')

    def get_queryset(self, request):
        qs = super(PreOrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(master=f"{Master.objects.get(user=request.user).name} "
                                f"{Master.objects.get(user=request.user).surname}")


class MasterAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(MasterAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class DateAdmin(admin.ModelAdmin):

    change_list_template = "admin/date_change_list.html"

    def get_urls(self):
        urls = super(DateAdmin, self).get_urls()

        custom_urls = [
            url('^add_week/$', self.add_week, name='add_week'),
        ]
        return custom_urls + urls

    @staticmethod
    def add_week(request):
        try:
            start_date = Date.objects.aggregate(Max('date'))['date__max']
            for date in add_days(start_date, 14):
                d = Date(date=date)
                d.save()
            return HttpResponseRedirect("../")
        except TypeError:
            start_date = datetime.date.today()
            for date in add_days(start_date, 14):
                d = Date(date=date)
                d.save()
            return HttpResponseRedirect("../")


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'date_joined')
    search_fields = ('id',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


admin.site.register(Order, OrderAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(PreOrder, PreOrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Time)
admin.site.register(Date, DateAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
