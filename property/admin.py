from django.contrib import admin

from .models import Flat, Complaint


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['town']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = [
        'new_building'
    ]
    list_filter = [
        'new_building',
        'has_balcony',
        'rooms_number'
    ]

    raw_id_fields = [
        'likes'
    ]


class ComplainsAdmin(admin.ModelAdmin):
    search_fields = [
        'flat',
        'user'
    ]
    list_display = [
        'user',
        'complaint',
        'flat'
    ]
    raw_id_fields = [
        'flat',
        'user'
    ]


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplainsAdmin)
