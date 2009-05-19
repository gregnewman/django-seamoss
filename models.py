import enums
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    """
    Base class for page content
    """

    #TODO check for sites

    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, help_text="This is a unique identifier that allows your page to display its detail view, ex 'this-is-my-title'")

    excerpt = models.TextField(_('Excerpt'), blank=True, null=True, help_text="This is a teaser of the body text; optional")
    body = models.TextField(_('Body'), blank=False, null=False)

    # flags
    published = models.BooleanField(_('Published'), default=True, help_text="If unchecked the page will not be accessible to users")

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
        return self.status == enums.STATUS_ACTIVE
