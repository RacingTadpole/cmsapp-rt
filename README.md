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
          'django_singleton_admin',
          'cmsapp_rt.bsglobals',
      )

2. Add the template context processor to your settings like this::
      
      from django_singleton_admin.admin import SingletonAdmin
      TEMPLATE_CONTEXT_PROCESSORS = (
          ...
          'cmsapp_rt.bsglobals.context_processors.globals',
      )

3. Extend the admin template "admin/base_site.py" using the base provided in
   django-singleton-admin, instead of the usual "admin/base.html", i.e. using:

        {% extends "admin/singleton_enabled_base.html" %}

   Note that this template uses the "extrastyle" block, so if you also override that, you
   will need to copy the contents of the provided template into your code instead.
   (In that case you may not need to add the app to your installed apps either.)

4. Run `python manage.py syncdb` (or use `python manage.py migrate` if you are using South) to create the models.

5. Run `python manage.py loaddata blank_globals` to set up a blank line in the table (this is required).

6. Look at cmsapp_rt/bsglobals/templates/base.html to see how to use this app in your templates.

