# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BSGlobalSettings'
        db.create_table('bsglobals_bsglobalsettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('head_placeholder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='head_placeholders', null=True, to=orm['cms.Placeholder'])),
            ('top_placeholder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='top_placeholders', null=True, to=orm['cms.Placeholder'])),
            ('pad_body_for_navbar_fixed_top', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('bsglobals', ['BSGlobalSettings'])


    def backwards(self, orm):
        # Deleting model 'BSGlobalSettings'
        db.delete_table('bsglobals_bsglobalsettings')


    models = {
        'bsglobals.bsglobalsettings': {
            'Meta': {'object_name': 'BSGlobalSettings'},
            'head_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'head_placeholders'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pad_body_for_navbar_fixed_top': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'top_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'top_placeholders'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['bsglobals']