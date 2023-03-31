from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Clients

def clients (request):
    if request.method == "POST":
        property_id = request.POST['property_id']
        property = request.POST['property']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_email = request.POST['owner_email']

        # Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/property/'+property_id)

        clients = Clients(property=property, property_id=property_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

        clients.save()

        # SEND EMAIL
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry fro ' + property + '. Sign in to the admin panel for more information.',
            'realestate@gmail.com',
            [owner_email, ],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a landlord will get back to you soon')
        return redirect('/property/'+property_id)

# Create your views here.
