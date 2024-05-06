from django.contrib import admin
from .models import *


class Doctor_CommentInline(admin.TabularInline):
    model = Doctor_C
    extra = 1


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0


@admin.register(Doctor_C)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'message', 'created', 'active']
    list_editable = ['active']


@admin.register(Web_user)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'birthday']
    inlines = [ReservationInline]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'expert', 'mc_number']
    inlines = [ReservationInline, Doctor_CommentInline]


admin.site.register(Reservation)
