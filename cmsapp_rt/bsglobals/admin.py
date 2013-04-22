from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin
from models import BSGlobalSettings

admin.site.register(BSGlobalSettings, PlaceholderAdmin)

