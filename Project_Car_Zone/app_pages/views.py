# Importing django modules
from django.shortcuts import render

# Create your views here.

# view for homepage
def view_home_page(request):
    return render(request, 'app_pages_templates/home.html')