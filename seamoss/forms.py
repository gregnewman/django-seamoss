from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _

from seamoss.models import Page, MenuItem
        
class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        exclude = ('markup',)
        
        
class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        exclude = ('lft', 'rght', 'tree_id', 'level', )