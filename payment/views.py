from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from property.models import Property
from .forms import PaymentForm

@login_required
def make_payment(request, property_id):
    property = Property.objects.get(id=property_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.property = property
            payment.save()
            return redirect('property_detail', property.id)
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_form.html', {'form': form, 'property': property})


# Create your views here.
