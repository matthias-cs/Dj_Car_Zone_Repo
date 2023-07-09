# Importing django modules
from django.shortcuts import render

# Create your views here.

# view for homepage
def view_home_page(request):
    return render(request, 'app_pages_templates/home.html')

# view for about page
def view_about_page(request):
    return render(request, "app_pages_templates/about.html")

# view for services page
def view_services_page(request):
    return render(request, "app_pages_templates/services.html")

# view for contact page
def view_contact_page(request):
    return render(request, "app_pages_templates/contact.html")