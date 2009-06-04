==============
Django-Seamoss
==============

django-seamoss is a simple cms to add to your django application to give your
administrators the ability to control parts of the site including pages, menus and
content blocks.

Installation:
=============

1. Put ``seamoss`` to your ``INSTALLED_APPS`` in your ``settings.py``
   within your django project.

2. Add ``url(r'^(?P<slug>[-_\w]+)/$', 'seamoss.views.render_page', name="render-page"),`` to your ``urls.py``.  It would be best to put it after your admin urls and any other important urls.

Features:
=========

1.  Unlimited menus providing the ability to create main navigation and sidebar navigations.
2.  Menu items can be linked to internal pages via a dropdown or external sites via a textfield.
3.  Markup language dropdown provided in the admin with a override for tinymce if it is installed.
4.  Basic key/value settings administration
5.  Creation of content blocks for use in sidebars, footers, etc.

Roadmap:
========

NOTE: Menus are not yet sortable via the admin.  While this app is stable on at least one site (http://beta.cis-pa.org) the menu system needs to be completed to provide
the ability to use up/down buttons to reorder the menu items.