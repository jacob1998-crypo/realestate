from django.contrib import admin

# Register your models here.



from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'property', 'payment_date', 'amount_paid',)
    list_display_links = ('id', 'user')
    search_fields = ('name', 'amount_paid', 'property')
    list_per_page = 25

admin.site.register(Payment, PaymentAdmin)