from django.urls import path

from . import views
app_name = "ecom"

urlpatterns = [
   # URL pattern for when page_no is provided
   path("<str:cat_url>/<int:page_no>/", views.index, name="index"),

   # URL pattern for when page_no is not provided (default to 1)
   path("", views.index, {'cat_url': 'winter-wear', 'page_no': 1}, name="index_default"),
]