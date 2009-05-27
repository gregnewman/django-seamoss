from datetime import date
from django import template
from django.template import Library, Node, Variable, TemplateSyntaxError, loader, TemplateDoesNotExist
from seamoss.models import Menu, MenuItem


register = Library()

class MenuNode(Node):
    def __init__(self, menuname, varname):
        self.menuname, self.varname = menuname, varname

    def render(self, context):
    	menu = Menu.objects.get(pk=self.menuname)
        context[self.varname] = MenuItem.objects.filter(menu=menu)
        return ''

def do_get_menu(parser, token):
    """
    returns menu items for a given menu id which must match a menu in the admin
    
    Example usage:
    {% get_menu 1 as menu %}

    """

    args = token.contents.split()
    if len(args) != 4:
        raise TemplateSyntaxError, "get_menu tag takes exactly three arguments"
    if args[2] != 'as':
        raise TemplateSyntaxError, "second argument to the get_menu tag must be 'as'"

    return MenuNode(args[1], args[3])
    
register.tag('get_menu', do_get_menu)