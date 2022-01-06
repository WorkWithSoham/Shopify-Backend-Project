from django.contrib import admin

from inventory.models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('ItemID', 'ItemName')
    ordering = ('ItemID', )
