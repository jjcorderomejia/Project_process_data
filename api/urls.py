from django.urls import path
from .views import TripView
from .views import load_trips_class

urlpatterns=[
    path('trips/', TripView.as_view(), name='trips_list'),
    path('load_trips/', load_trips_class.as_view(), name='load_trips_list')
]