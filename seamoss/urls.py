from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
    url(r'^admin_move/(?P<direction>up|down)/(?P<menuitem_id>\d+)/$',
        view = 'seamoss.views.admin_move_menu_item',
        name="admin_move"),

    url(r'^(?P<slug>[-_\w]+)/$',
        view = 'seamoss.views.render_page',
        name="render-page"),

    url(r'^$',
        view = 'seamoss.views.home_page',
        name="home-page"),
)
