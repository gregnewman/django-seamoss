from django.conf import settings

# The default site id to be used for multiple site support.
SITE_ID = getattr(settings, 'SITE_ID', 1)
