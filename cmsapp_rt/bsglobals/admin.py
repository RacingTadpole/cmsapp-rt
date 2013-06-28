from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from django_singleton_admin.admin import SingletonAdmin
from models import BSGlobalSettings

class BSGlobalSettingsAdmin(PlaceholderAdmin, SingletonAdmin):
    pass

admin.site.register(BSGlobalSettings, BSGlobalSettingsAdmin)

