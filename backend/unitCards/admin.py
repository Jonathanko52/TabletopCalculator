from django.contrib import admin
from .models import Character, Weapon

class WeaponInline(admin.TabularInline):
    model = Weapon
    extra = 1  # Number of empty forms to show
    fields = ('name', 'range', 'A', 'WS', 'S', 'AP', 'D', 'keywords')
    show_change_link = True

# @admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'M', 'T', 'SV', 'W', 'LD', 'OC')
    search_fields = ('name',)
    inlines = [WeaponInline]

# @admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'character', 'range', 'A', 'WS', 'S', 'AP', 'D')
    search_fields = ('name', 'character__name')
    list_filter = ('character',)

admin.site.register(
    Weapon,
    WeaponAdmin)
admin.site.register(
    Character,
    CharacterAdmin,
)