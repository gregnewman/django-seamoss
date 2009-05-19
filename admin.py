from django.contrib import admin
from models import *
from django.db.models import get_model
from reversion.admin import VersionAdmin

class PageAdmin(VersionAdmin):
    ordering = ('title',)
    list_display = ('title', 'published', 'created_on')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    
admin.site.register(get_model('seamoss', 'page'), PageAdmin)

