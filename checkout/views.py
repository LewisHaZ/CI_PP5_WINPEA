from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O7e32EaTuQRySZMBby6ySIb0JBTPIkXpQWlfW5rFKL4wjzdijUHempAOfrvX5Mg9YX5kfuKcZkQuvBwPE57Bt36003zfkoDqk',
        'client_secret': 'test',
    }

    return render(request, template, context)