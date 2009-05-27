from datetime import datetime
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
import mptt
from seamoss import settings

try:
    tagging = models.get_app('tagging')
    from tagging.fields import TagField
except ImproperlyConfigured:
    tagging = False

#TODO move this to settings.py
try:
    markup_choices = settings.SEAMOSS_MARKUP_CHOICES
except AttributeError:
    markup_choices = (
        ('txl', _(u'Textile')),
        ('mrk', _(u'Markdown')),
        ('rst', _(u'reStructuredText')),
    )
    
class Page(models.Model):
    """
    Base class for page content
    """
	
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True, help_text=_("This is a unique identifier that allows your page to display its detail view, ex 'this-is-my-title'"))

    excerpt = models.TextField(_('Excerpt'), blank=True, null=True, help_text=_("This is a teaser of the body text; optional"))
    body = models.TextField(_('Body'), blank=False, null=False)

    # markup
    markup = models.CharField(_("Content Markup"), max_length=3, choices=markup_choices, null=True, blank=True)
    
    # Meta
    keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)
    description = models.TextField(_('Meta Description'), null=True, blank=True)
    if tagging:
        tags = TagField()

    # relations
    related_content = models.ManyToManyField("self", null=True, blank=True)
    sites = models.ManyToManyField(Site, default=[settings.SITE_ID])
    
    # flags
    published = models.BooleanField(_('Published'), default=True, help_text=_("If unchecked the page will not be accessible to users"))

    # dates
    publish_on = models.DateTimeField(_('Publish On'), null=True, blank=True)
    expire_on = models.DateTimeField(_('Expire On'), null=True, blank=True)

    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by")
    created_on = models.DateTimeField(_('Created On'), default=datetime.now, editable=False)
    updated_on = models.DateTimeField(_('Updated On'), editable=False)
    updated_by = models.ForeignKey(User, null=True, editable=False) 

    class Meta:
        ordering = ['created_on', ]

    def __unicode__(self):
        return self.title

    def save(self):
        self.updated_on = datetime.now()
        super(Page, self).save()

    def is_published(self):
        return self.published


class Menu(models.Model):
    """
    Base class for menus
    Multiple menus are supported so a site can have a main navbar and subnavs
    """

    title = models.CharField(_('Title'), max_length=200, help_text=_("Used only to differentiate the menus"))
    description = models.TextField(_('Description'), null=True, blank=True, help_text=_("A brief description of the menu"))

    # associations
    parent = models.ForeignKey("self", blank=True, null=True, help_text=_("If this menu is a subnavigation menu, assign it it's parent menu"))
    sites = models.ManyToManyField(Site, default=[settings.SITE_ID])
    
    # flags
    published = models.BooleanField(_('Published'), default=True, help_text=_("If unchecked the menu will not be visible to users"))

    # page assignment
    # use to assign menus to show on certain pages only. handy for special submenus
    show_on_pages = models.ManyToManyField(Page, null=True, blank=True, help_text=_("If you want a page to show this menu as a sub menu select which page(s) here"))

    # dates
    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by")
    created_on = models.DateTimeField(_('Created On'), default=datetime.now, editable=False)
    updated_on = models.DateTimeField(_('Updated On'), editable=False)
    updated_by = models.ForeignKey(User, null=True, editable=False) 

    class Meta:
        ordering = ['created_on', ]

    def __unicode__(self):
        return self.title

    def save(self):
        self.updated_on = datetime.now()
        super(Menu, self).save()


class MenuItem(models.Model):
    """
    Base class for menu items.
    An item can be assigned to multiple menus
    and does not have to be a page in the cms
    """

    name = models.CharField(_('Link Text'), max_length=200, help_text=_("This is what displays in the menu"))
    menu = models.ForeignKey(Menu)
    internal_item = models.ForeignKey(Page, null=True, blank=True)
    external = models.BooleanField(_('External Link'), default=False, help_text=_("If this link goes to a external site check this box"))
    external_link = models.URLField(_('Link URL'), verify_exists=True, max_length=200, blank=True, null=True)

    # parenting
    parent = models.ForeignKey("self", blank=True, null=True, help_text=_("If this item is a child of another item, assign it's parent"))
    
    # dates
    created_by = models.ForeignKey(User, null=True, editable=False, related_name="%(class)s_created_by")
    created_on = models.DateTimeField(_('Created On'), default=datetime.now, editable=False)
    updated_on = models.DateTimeField(_('Updated On'), editable=False)
    updated_by = models.ForeignKey(User, null=True, editable=False) 


    class Meta:
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    def save(self):
        self.updated_on = datetime.now()
        super(MenuItem, self).save()
        
    @models.permalink
    def get_absolute_url(self):
    	if not self.external:
    		return ('render-page', (), {
    	        'slug': self.internal_item.slug,
        	})
    	else:
	    	return ""


# Don't register the Page model twice.
try:
    mptt.register(MenuItem)
except mptt.AlreadyRegistered:
    pass
