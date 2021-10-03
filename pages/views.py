from django.core.mail import send_mail
from django.shortcuts import render
from listings.choices import price_choices, state_choices, garage_choices, garden_choices

from listings.models import Listing


def home(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'garage_choices': garage_choices,
    }

    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        textarea = request.POST['textarea']

        # Send an email
        send_mail(
            'message from ' + message_name,  # subject
            textarea,  # message
            message_email,  # from email
            ['djangotest62@gmail.com'],  # to email
        )

        return render(request, 'pages/contact.html', {'message_name': message_name})

    else:
        return render(request, 'pages/contact.html', {})
