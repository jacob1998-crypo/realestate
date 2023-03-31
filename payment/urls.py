from django.urls import path
from .views import make_payment

urlpatterns = [
    path('make_payment/<int:property_id>/',views.make_payment, name='make_payment'),
]
