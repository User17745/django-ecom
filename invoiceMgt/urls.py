from django.urls import path, include
from rest_framework import routers
from .views import InvoiceViewSet
from . import views

app_name = "invoiceMgt"

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    # ... other URL patterns ...
    path('api/', include(router.urls)),
]
