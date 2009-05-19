from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def render_page(request, slug):
    """
    Displays the page matching the given slug
    """

    page = user = get_object_or_404(Page, slug=slug)
    
    return render_to_response('seamoss/page.html', {
        "page": page,
    }, context_instance=RequestContext(request))


#TODO add in a preview view for admin previews
