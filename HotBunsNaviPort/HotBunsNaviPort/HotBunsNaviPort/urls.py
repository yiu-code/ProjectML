"""
Definition of urls for HotBunsNaviPort.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

# Als je deze Url intikt, dat voert het dit stuk code uit. Bij bijvoorbeeld login dan gaat het diect naar het bestand, en skipt het de views.py. Bij '^$' (Blanko) Dat execute het home bij de view. Je geeft het een naam zodat je via deze naam de link kan plaatsen op een webpagina zelf. 
urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
