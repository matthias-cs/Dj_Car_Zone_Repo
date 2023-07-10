# PYTHON builtin modules
import os, sys
# 3rd party PYTHON modules  
import colorama
from colorama import Fore, Back, Style # importing foreground background and style libraries

# DJANGO modules
from django.db import models

# Create your models here.
class TeamMemberOfCompany(models.Model):
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
    first_name = models.CharField(max_length=256,)
    last_name = models.CharField(max_length=256,)
    designation = models.CharField(max_length=256,)
    photo = models.ImageField(upload_to="Photo_For_Company_teams/%y/%m/%d")
    facebook_url = models.URLField(max_length=120)
    google_plus = models.URLField(max_length=120)
    twitter_url = models.URLField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_all_team_members(cls) -> dict:
        try:
            # the action below might raise an exception
            queryset_all_team_members = TeamMemberOfCompany.objects.all()

        except Exception as e:     
            print(f"{Fore.RED}{Style.BRIGHT}____Exception occured ")
            print(f"{Fore.RED}{Style.BRIGHT}Function name = view_EPA_Documents() in Views ")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{Fore.RED}{Style.BRIGHT}Details ", f"{Fore.RED}{Style.BRIGHT}{exc_type}", f"{Fore.RED}{Style.BRIGHT}{fname}", f"{Fore.RED}{Style.BRIGHT}{exc_tb.tb_lineno}")
            print(f"{Fore.RED}{Style.BRIGHT} The exception =>  ", e)
            print(f"{Fore.RED}{Style.BRIGHT}____ Exception ends here ")       
            return {
                "was_execution_successful":True,
                "the_returned_value": queryset_all_team_members,
            }
        else:
            # This block runs "on success"
            return {
                "was_execution_successful":True,
                "the_returned_value": queryset_all_team_members,
            }
