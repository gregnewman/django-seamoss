from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)/$', 'seamoss.views.render_page', name="render-page"),
    url(r'^$', 'seamoss.views.home_page', name="home-page"),
)
