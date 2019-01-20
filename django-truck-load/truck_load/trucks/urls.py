from django.conf.urls import url
from . import views

urlpatterns = [

    # Trucks
    url(
        r'^api/v1/truck/(?P<pk>[0-9]+)$',
        views.get_delete_update_truck,
        name='get_delete_update_truck'
    ),
    url(
        r'^api/v1/trucks/$',
        views.get_post_trucks,
        name='get_post_trucks'
    ),

    # Loads
    url(
        r'^api/v1/load/(?P<pk>[0-9]+)$',
        views.get_delete_update_load,
        name='get_delete_update_load'
    ),
    url(
        r'^api/v1/loads/$',
        views.get_post_loads,
        name='get_post_loads'
    ),

    # The entry point for the algorithm to map trucks to loads
    url(
        r'^api/v1/map_trucks_to_loads/$',
        views.get_map_trucks_to_loads,
        name='get_map_trucks_to_loads'
    )
]