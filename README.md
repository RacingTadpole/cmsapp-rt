=====
cmsapp-rt
=====

This package contains one app (including a context processor and example template) to help your Django-CMS project
work with Twitter Bootstrap.

You may also find the cmsplugin-rt package helpful with this,
e.g. to provide a navbar in the placeholder provided.

Detailed documentation will be added to the "docs" directory.

Requirements
--------------

I built these using:

* Django 1.4
* Django-CMS 2.3.5
* South
* django-singleton-admin

Quick start
-----------

1. Add the app to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'cmsapp_rt.bsglobals',
      )

2. Add the template context processor to your settings like this::

      TEMPLATE_CONTEXT_PROCESSORS = (
          ...
          'cmsapp_rt.bsglobals.context_processors.globals',
      )


3. Run `python manage.py syncdb` (or use `python manage.py migrate` if you are using South) to create the models.

4. Run `python manage.py loaddata blank_globals` to set up a blank line in the table (this is required).

5. Look at cmsapp_rt/bsglobals/templates/base.html to see how to use this app in your templates.

