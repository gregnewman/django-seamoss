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

class MenuAdmin(VersionAdmin):
    ordering = ('title',)
    list_display = ('title', 'published', 'created_on')
    list_filter = ('published',)
    save_on_top = True

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on',)
    
admin.site.register(get_model('seamoss', 'page'), PageAdmin)
admin.site.register(get_model('seamoss', 'menu'), MenuAdmin)
admin.site.register(get_model('seamoss', 'menuitem'), MenuItemAdmin)
