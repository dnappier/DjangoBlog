
from django.conf.urls import patterns,  url

urlpatterns = patterns('', 
                       url(r'^all/$', 'djangoblog.views.posts'),
                       url(r'^posting(?P<posting_id>\d+)/$', 'djangoblog.views.posting_individual'),
)