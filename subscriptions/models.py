from django.db import models
# import secrets
# from .paystack import PayStack
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    ad_detail = models.TextField(blank=True, null=True)
    chat_detail = models.TextField(blank=True, null=True)
    coverage_detail = models.TextField(blank=True, null=True)
    boosted_listing_detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        Subscription, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subscription.name


# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subscription = models.ForeignKey(
#         Subscription, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
#     ref = models.CharField(max_length=200)
#     email = models.EmailField()
#     verified = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date_created']

#     def __str__(self):
#         return f"Payment: {self.subscription.name}"

#     def save(self, *args, **kwargs):
#         while not self.ref:
#             ref = secrets.token_urlsafe(50)
#             object_with_similar_ref = Payment.objects.filter(ref=ref)
#             if not object_with_similar_ref:
#                 self.ref = ref
#         super().save(*args, **kwargs)

#     def amount_value(self):
#         return self.subscription.price * 100

#     def verify_payment(self):
#         paystack = PayStack()
#         status, result = paystack.verify_payment(
#             self.ref, self.subscription.price)
#         if status:
#             if result['subscription.price'] / 100 == self.subscription.price:
#                 self.verified = True
#             self.save()
#         if self.verified:
#             return True
#         return False

