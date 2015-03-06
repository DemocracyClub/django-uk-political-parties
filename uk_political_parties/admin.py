from django.contrib import admin
from .models import Party, PartyEmblem

class PartyEmblemInline(admin.TabularInline):
    model = PartyEmblem

class PartyAdmin(admin.ModelAdmin):
    inlines = [PartyEmblemInline, ]

admin.site.register(Party, PartyAdmin)
