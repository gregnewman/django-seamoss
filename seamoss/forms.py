from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _

from seamoss.models import Page
        
class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        exclude = ('markup',)