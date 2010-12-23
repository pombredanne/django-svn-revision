# $Id: django-revision.py $
# Authors: Sean Auriti <sa@alexanderinteractive.com>, David Napolitan <dn@alexanderinteractive.com>
# Updated by Chris Gilmer on 2010/12/22

"""
Creates a template tag called {% revision %} that returns the current svn version.
Requires svnversion.
"""

import sys, os
from django import template
from svnrevision.templatetags import get_revision

register = template.Library()

@register.simple_tag
def revision():
    """
	displays the revision number
    
    {% revision %}
	"""
    return get_revision()
