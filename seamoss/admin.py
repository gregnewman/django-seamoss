from django.contrib import admin
from models import *
from django.db.models import get_model
from reversion.admin import VersionAdmin
from seamoss.forms import PageForm

try:
    tinymce = models.get_app('tinymce')
except ImproperlyConfigured:
    tinymce = False

class PageAdmin(VersionAdmin):
    ordering = ('title',)
    list_display = ('title', 'published', 'created_on')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    if tinymce:
        form = PageForm

class MenuAdmin(VersionAdmin):
    ordering = ('title',)
    list_display = ('title', 'published', 'created_on')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

class BlockAdmin(VersionAdmin):
    ordering=('name',)
    list_display = ('name', 'slug', 'created_on')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on', 'menu', 'order_link',)
    
class SettingAdmin(admin.ModelAdmin):
    ordering = ('setting_key',)
    list_display = ('setting_key', 'setting_value',)
    
admin.site.register(get_model('seamoss', 'page'), PageAdmin)
admin.site.register(get_model('seamoss', 'block'), BlockAdmin)
admin.site.register(get_model('seamoss', 'menu'), MenuAdmin)
admin.site.register(get_model('seamoss', 'menuitem'), MenuItemAdmin)
admin.site.register(get_model('seamoss', 'cmssetting'), SettingAdmin)
