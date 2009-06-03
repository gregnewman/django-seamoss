from datetime import date
from django import template
from django.template import Library, Node, Variable, TemplateSyntaxError, loader, TemplateDoesNotExist
from seamoss.models import Menu, MenuItem


register = Library()

class MenuNode(Node):
    def __init__(self, menuname, varname):
        self.menuname, self.varname = menuname, varname
        
    def resolve(self, var, context):
        """Resolves a variable out of context if it's not in quotes"""
        if var[0] in ('"', "'") and var[-1] == var[0]:
            return var[1:-1]
        else:
            return Variable(var).resolve(context)

    def render(self, context):
        menuname = self.resolve(self.menuname, context)
        if self.varname:
            varname = self.resolve(self.varname, context)
        else:
            varname = 'menu'

    	menu = Menu.objects.get(slug=menuname)
        context[varname] = MenuItem.objects.filter(menu=menu)
        return ''

@register.tag
def get_menu(parser, token):
    """
    returns menu items for a given menu slug which must match a menu in the admin
    
    Example usage:
    {% get_menu slug as menu %}

    """

    args = token.contents.split()
    if len(args) != 4:
        raise TemplateSyntaxError, "get_menu tag takes exactly three arguments"
    if args[2] != 'as':
        raise TemplateSyntaxError, "second argument to the get_menu tag must be 'as'"

    return MenuNode(args[1], args[3])