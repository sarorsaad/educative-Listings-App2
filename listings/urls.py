from django.urls import path
from .import views


app_name = 'listings'

urlpatterns = [
    # Homepage
    path(' ', views.all_listings, name='all_listings'),
    # Listings Page
    path('all_listings/', views.all_listings, name='all_listings'),
   
]
