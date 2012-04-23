django-snippets
===============

A really small django CMS

This a django app intended to be dropped into an existing django project to allow editing of 
predefined regions in a template, through use of a custom template tag. The regions can be unique,
(e.g. a block of welcome text on a homepage) or shared across templates (e.g. footer text).

Snippets are created by adding the custom template tag, with a unique slug - if a snippet doesn't already 
exist with the specified slug, it will automatically be created.

In its most basic form, when a user logs into the standard django admin then returns to the site,
each snippet is outlined and contains an edit link, taking the user to the appropriate edit screen
in the django admin. With the basic javascript enabled, the user will instead be able to edit the
snippet HTML in a pop-up window.

To install, add the snippets folder to your django project, then enable the app and template tags by adding
to your INSTALLED_APPS:-

```
    'snippets',
    'snippets.templatetags',
```

(Obviously the you'll need to syncdb stuff to have the SQL created for the snippet model)

To add a snippet to a template, first include snippet_extras:-

```{% load snippet_extras %}```

Then add a tag in the following format:-

```{% get_snippet "footer" %}```

The "slug" (the part in quotes above needs) to be in a suitable format to form part of a URL, so use 
letters, numbers and hyphens (no spaces or other special characters that would break a URL)