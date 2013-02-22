# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.subtitle'
        db.delete_column('portfolio_project', 'subtitle')


    def backwards(self, orm):
        # Adding field 'Project.subtitle'
        db.add_column('portfolio_project', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    models = {
        'portfolio.project': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['portfolio']