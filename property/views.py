from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choice import price_choices, bedroom_choices, state_choices 

from .models import Property


def index(request):
    property = Property.objects.order_by('-property_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_property = paginator.get_page(page)

    context = {
        'property': paged_property
        
    }

    return render(request, 'property/property.html', context)


def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property
    }

    return render(request, 'property/property.html', context)


def search(request):
    queryset_list = Property.objects.order_by('-property_date')

    # KEYWORDS
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # CITY
    if 'location' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # STATE
    if 'county' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # BEDROOMS
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # PRICE
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'property/search.html', context)


# Create your views here.
