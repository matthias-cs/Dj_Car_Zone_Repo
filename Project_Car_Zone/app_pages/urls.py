
# Importing django modules
from django.urls import path

# Importing project modules
from .views import view_home_page, view_about_page, view_services_page, view_contact_page 
urlpatterns = [
    path('', view_home_page, name="url_name_for_home_page"),
    path('about', view_about_page, name="url_name_for_about_page"),
    path('services', view_services_page, name="url_name_for_services_page"),
    path('contact', view_contact_page, name="url_name_for_contact_page"),
]