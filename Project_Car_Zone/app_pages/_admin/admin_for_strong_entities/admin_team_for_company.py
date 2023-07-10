# Python Modules
from datetime import date

# PYTHON 3rd Party Modules
import colorama
from colorama import Fore, Back, Style # importing foreground background and style libraries

# Django Modules
from django.contrib import admin
from django.utils.html import format_html


# project Modules | Modules from this project
    # ---- Model Imports
from ..._models.strong_entities.model_TeamMemberOfCompany import TeamMemberOfCompany

    # ---- Filter Modules being imported
# from .ADMIN_FILTERS.FIlter_Searchable_Dropdown.Collector_Model.Collector_Model_Used_Battery_Type_Searchable_Dropdown_Filter.Used_Battery_Type_Searchable_Dropdown import *



# ADMIN VIEW
class AdminViewForTeamOfCompany(admin.ModelAdmin):
    class Media:
        css = {
            'all': [
                    # settings.STATIC_URL + 'CSS/bootstrap-5.0.2-dist/css/bootstrap.min.css',
                    # settings.STATIC_URL + 'CSS\Custom_CSS\google_maps\map_preview.css',
                    ]
            }
        js = (
            #   settings.STATIC_URL + 'JS/Custom_JS/Google_Maps_Js/maps_preview.js', 
        )

    # actions = ['action_export_to_excel'] # no need for this
    fieldsets = []
    filter_horizontal = []
    # fields = [('battery_distribution_year', 'battery_distribution_quarter'),('battery_source', 'battery_type'),\
    #             'distributed_battery_amount_in_KG','additional_note']
    # inlines = [InlineMembersNoneRelated]
    list_per_page = 1
    list_display = ['first_name','last_name','designation', 'list_view_photo', 'created_date']
    list_display_links = ['first_name','last_name','designation', 'created_date']
    # list_select_related = ('member',)
    # list_editable = []
    list_filter = ['designation',]
    search_fields = []
    list_per_page = 10
    search_fields = ('first_name', 'last_name', 'designation')
    def list_view_photo(self, model_object):
        if model_object.photo:
            return format_html(f"\
                               <a href='{model_object.photo.url}'>\
                                    <img src='{model_object.photo.url}' style='width:8em; border-radius:2em;' \
                                    alt='Photo of team member'>\
                               </a>\
                               ")
        else:
            return "No photo"
        
    list_view_photo.short_description = 'Photo'

admin.site.register(TeamMemberOfCompany, AdminViewForTeamOfCompany )