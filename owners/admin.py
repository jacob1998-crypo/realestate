from django.contrib import admin

from .models import Owners

class OwnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Owners, OwnersAdmin)


# Register your models here.
