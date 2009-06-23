from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _

from seamoss.models import Page, MenuItem
        
class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        exclude = ('markup',)