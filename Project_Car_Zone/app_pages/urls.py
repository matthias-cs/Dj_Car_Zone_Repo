
# Importing django modules
from django.urls import path

# Importing project modules
from .views import view_home_page
urlpatterns = [
    path('', view_home_page, name="url_name_for_home_page"),
]