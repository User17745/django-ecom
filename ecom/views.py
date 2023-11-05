from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render #shortcuts to handle template loading, and try-catch for resource unavailable.
import requests, json


def index(request, cat_url="winter-wear", page_no=1):
    per_page_product_count = 16

    plp = call_api(f"https://getketchpim.getketch.com/pim/pimresponse.php/?service=category&store=1&url_key={cat_url}&page={page_no}&count={per_page_product_count}&sort_by=&sort_dir=desc&filter=");
    # return HttpResponse(json.dumps(plp))

    # total_page_count = plp.result.count / per_page_product_count;
    context = {"callback" : plp, "cat_url": cat_url, "current_page_no": page_no, "next_page_no": page_no+1, "prev_page_no": page_no-1, "total_page_count": 100} 
    return render(request, "ecom/index.html", context)

def call_api(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            # Process the data as needed
            return data
        else:
            # Handle errors appropriately
            print(f"API request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle network or request errors
        print(f"Request exception: {e}")
        return None
