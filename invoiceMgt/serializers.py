from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    # Create serializer fields for client and service names
    client_name = serializers.ReadOnlyField(source='client.name')
    service_name = serializers.ReadOnlyField(source='service.service')
    # payment_status = serializers.ReadOnlyField(source='invoice.payment_status')

    class Meta:
        model = Invoice
        fields = '__all__'  # You can specify the fields you want to include in the API response