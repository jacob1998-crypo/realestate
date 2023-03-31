from django.shortcuts import render
from django.http import HttpResponse
from property.choice import price_choices, bedroom_choices, state_choices 

from property.models import Property
from owners.models import Owners

def index(request):
    propertys = Property.objects.order_by('-list_date')

    context = {
        'propertys': propertys,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
   owners = Owners.objects.order_by('-hire_date')

    # Get MVP
   mvp_owners = Owners.objects.all().filter(is_mvp=True)

   context = {
        'owners': owners,
        'mvp_owners': mvp_owners
    }

   return render(request, 'pages/about.html', context)


# Create your views here.
