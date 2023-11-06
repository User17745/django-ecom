from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

    
class Client(models.Model):
    name = models.CharField(max_length=200)
    poc_name = models.CharField(max_length=200)
    poc_phone = models.CharField(max_length=15)
    poc_email = models.EmailField(max_length=50)
    def __str__(self):
        return self.name

class Service(models.Model):
    service = models.CharField(max_length=200)
    def __str__(self):
        return self.service

class Invoice(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('1', 'Received'),
        ('0', 'Pending'),
    ]

    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('cheq', 'Cheque'),
        ('neft', 'NEFT'),
        ('rtgs', 'RTGS'),
        ('imps', 'IMPS'),
        ('upi', 'UPI'),
        ('cc', 'Credit Card'),
        ('dc', 'Debit Card'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=30)
    narration = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True ,choices=PAYMENT_STATUS_CHOICES)
    payment_mode = models.CharField(max_length=20, blank=True, null=True, choices=PAYMENT_MODE_CHOICES)
    payment_ref_number = models.CharField(max_length=50, blank=True, null=True)
    payment_date = models.DateTimeField("Paid on", blank=True, null=True)
    due_date = models.DateTimeField("Last payable by")
    billed_date = models.DateTimeField("Date billed", default=timezone.now)

    def __str__(self):
        return self.invoice_number
    def was_billed_recently(self):
        return self.billed_date >= timezone.now() - datetime.timedelta(days=2)
    def was_paid_recently(self):
        return self.payment_date >= timezone.now() - datetime.timedelta(days=2)
    def is_due_soon(self):
        return self.due_date >= timezone.now() - datetime.timedelta(days=7)