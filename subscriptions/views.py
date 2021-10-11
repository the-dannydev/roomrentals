from django.conf import settings
from django.contrib import messages
from .models import Subscription, Order, Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import JsonResponse
from .forms import PaymentForm
import json

# Paypal Integration

def subscription(request):
    subscriptions = Subscription.objects.all()
    context = {'subscriptions': subscriptions}
    return render(request, 'subscriptions/subscription.html', context)


def checkout(request, pk):
    subscription = Subscription.objects.get(id=pk)
    context = {'subscription': subscription}
    return render(request, 'subscriptions/checkout.html', context)


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    subscription = Subscription.objects.get(id=body['productId'])
    Order.objects.create(
        subscription=subscription
    )

    return JsonResponse('Payment completed!', safe=False)


# Paystack Integration

def initiate(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            return render(request, 'paystack.html', {
                   'payment': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = PaymentForm()
    return render(request, 'initiate.html', {'payment_form': payment_form})


def verify_payment(request, ref):
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification successful!")
    else:
        messages.error(request, "Verification failed")
    return redirect('initiate-payment')
