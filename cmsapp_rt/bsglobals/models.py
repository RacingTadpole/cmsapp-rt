from django.utils.translation import ugettext_lazy as _
from django.db import models

from cms.models.fields import PlaceholderField

class BSGlobalSettings(models.Model):
    head_placeholder = PlaceholderField('head_placeholder', related_name="head_placeholders")
    top_placeholder = PlaceholderField('top_placeholder', related_name="top_placeholders")
    pad_body_for_navbar_fixed_top = models.IntegerField(_("Body padding"), null=True, blank=True,
                            help_text=_('Optional. Pads the top of the main body by this many pixels. Bootstrap recommends to use at least 40 if your navbar is fixed to the top (see http://twitter.github.com/bootstrap/components.html#navbar).'))
    
    def __unicode__(self):
        return u"Appearance"
    class Meta:
        verbose_name = "Appearance"
        verbose_name_plural = "Appearance"

