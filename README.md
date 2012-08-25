# Django-svn-revision - Abandoned

Creates a template tag called ``{% revision %}`` that returns the current svn version.

## Usage:
1.  Include the app in your ``settings.py`` file
2.  Load the templatetag: ``{% load revision %}``
3.  Include ``{% revision %}`` in your template file.
4.  Make sure you have set PROJECT_ROOT in your settings.py file

## Notes:
* Requires ``svnversion`` to be installed.
