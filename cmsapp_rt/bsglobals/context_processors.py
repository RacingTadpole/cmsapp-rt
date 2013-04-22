from models import *
from django.shortcuts import get_object_or_404

def globals(request):
    g = get_object_or_404(BSGlobalSettings, pk=1)
    return {'BSGLOBAL': g}
