from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='agenda.html')),
    url(r'^eventsXML$', 'apps.agenda.views.eventsXML', name='eventsXML'),
    url(r'^dataprocessor$', 'apps.agenda.views.dataprocessor', name='dataprocessor'),

)
