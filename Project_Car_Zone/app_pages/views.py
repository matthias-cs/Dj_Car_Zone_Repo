# Importing django modules
from django.shortcuts import render

# Importing project modules
from ._models.strong_entities.model_TeamMemberOfCompany import TeamMemberOfCompany as TeamMembers

# Create your views here.

# view for homepage
def view_home_page(request):
    attempt_to_get_queryset = TeamMembers.get_all_team_members()
    if attempt_to_get_queryset['was_execution_successful']:
        queryset_all_team_members = attempt_to_get_queryset['the_returned_value']
    else:
        queryset_all_team_members = None
    data_for_rendering_page = {
        'team_members': queryset_all_team_members,
        }
    return render(request, 'app_pages_templates/home.html', data_for_rendering_page)

# view for about page
def view_about_page(request):
    attempt_to_get_queryset = TeamMembers.get_all_team_members()
    if attempt_to_get_queryset['was_execution_successful']:
        queryset_all_team_members = attempt_to_get_queryset['the_returned_value']
    else:
        queryset_all_team_members = None
    data_for_rendering_page = {
        'team_members': queryset_all_team_members,
        }
    return render(request, "app_pages_templates/about.html", data_for_rendering_page)

# view for services page
def view_services_page(request):
    return render(request, "app_pages_templates/services.html")

# view for contact page
def view_contact_page(request):
    return render(request, "app_pages_templates/contact.html")