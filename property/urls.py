from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='property'),
    path('<int:property_id>', views.property, name='property'),
    path('search', views.search, name='search')
]
