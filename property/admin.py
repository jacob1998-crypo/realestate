from django.contrib import admin

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'price', 'property_date', 'owner')
    list_display_links = ('id', 'title')
    list_filter = ('owner',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price')
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)


# Register your models here.
