from django.contrib import admin

from menu.models import MenuItem, Menu


class MenuItemInLine(admin.TabularInline):
    model = MenuItem
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInLine]

admin.site.register(Menu, MenuAdmin)
