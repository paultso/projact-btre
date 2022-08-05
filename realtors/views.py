from .models import Listing
from .choices import price_choices, state_choices,
from django.shortcuts import get_object_or_404, render
# import the 404 as well
from django.core.paginator import EmptyPage,
PageNotAnInteger, Paginator

# choices at the same folder
bedroom_choices
# load database into view


def index(request):
    listings = Listing.objects.order_by('-list_date').
    filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

# Create your views here.
