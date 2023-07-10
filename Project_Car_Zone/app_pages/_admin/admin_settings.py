# Python Modules
import colorama
from colorama import Fore, Back, Style # importing foreground background and style libraries

# Django Modules
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Django 3rd Party Modules


#___________Python colorful terminal text with colorama 
colorama.init(autoreset=True)
    # ____________________ Colorama Options
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL`


# print("\033[31m_______ inside ADMIN_SETTINGS.py") # print with color red
print(f"{Fore.GREEN}{Style.BRIGHT}___ inside admin_settings.py ___") # print with color red
# print('\033[39m') # USE DEFAULT STYLE AFTER THIS

# ____________________ Admin Codes
#admin site customization
admin.site.site_header = format_html(f"<h1 style='text-align: center; display:inline; margin:10px;' > Car Zone Admin </h1>")
admin.site.site_title = format_html('Car Zone Admin ')

admin.site.index_title = 'Site administration'
