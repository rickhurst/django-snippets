from django.conf.urls.defaults import *
from snippets import views
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
    '',
    
     (r'^snippets/edit-snippet/(?P<slug>[\w-]+)/(?P<mode>[\w-]+)', 'snippets.views.edit_snippet'),
    
)
