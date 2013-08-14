# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MultipleSelect'
        db.create_table(u'survey_multipleselect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('option', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'survey', ['MultipleSelect'])

        # Adding model 'Preliminary1'
        db.create_table(u'survey_preliminary1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmailUser'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('marital_status', self.gf('django.db.models.fields.IntegerField')()),
            ('in_person_contact', self.gf('django.db.models.fields.IntegerField')()),
            ('formal_education', self.gf('django.db.models.fields.IntegerField')()),
            ('new_relation', self.gf('django.db.models.fields.IntegerField')()),
            ('cope_stress', self.gf('django.db.models.fields.IntegerField')()),
            ('current_work', self.gf('django.db.models.fields.IntegerField')()),
            ('work_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('work_week', self.gf('django.db.models.fields.IntegerField')()),
            ('brain_activity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'survey', ['Preliminary1'])

        # Adding M2M table for field source_of_stress on 'Preliminary1'
        m2m_table_name = db.shorten_name(u'survey_preliminary1_source_of_stress')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('preliminary1', models.ForeignKey(orm[u'survey.preliminary1'], null=False)),
            ('multipleselect', models.ForeignKey(orm[u'survey.multipleselect'], null=False))
        ))
        db.create_unique(m2m_table_name, ['preliminary1_id', 'multipleselect_id'])

        # Adding model 'Preliminary2'
        db.create_table(u'survey_preliminary2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmailUser'])),
            ('air_pollution', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('seatbelt', self.gf('django.db.models.fields.IntegerField')()),
            ('coffee', self.gf('django.db.models.fields.IntegerField')()),
            ('second_smoke', self.gf('django.db.models.fields.IntegerField')()),
            ('often_smoke', self.gf('django.db.models.fields.IntegerField')()),
            ('many_smoke', self.gf('django.db.models.fields.IntegerField')()),
            ('exposure_smoke', self.gf('django.db.models.fields.IntegerField')()),
            ('lung_disease', self.gf('django.db.models.fields.IntegerField')()),
            ('day_alcohol', self.gf('django.db.models.fields.IntegerField')()),
            ('glass_alcohol', self.gf('django.db.models.fields.IntegerField')()),
            ('aspirin', self.gf('django.db.models.fields.IntegerField')()),
            ('floss_teeth', self.gf('django.db.models.fields.IntegerField')()),
            ('sunscreen', self.gf('django.db.models.fields.IntegerField')()),
            ('body_mass_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'survey', ['Preliminary2'])

        # Adding model 'Preliminary3'
        db.create_table(u'survey_preliminary3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmailUser'])),
            ('bowel_movement', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('skin_cancer', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('heart_attack', self.gf('django.db.models.fields.IntegerField')()),
            ('doctor_appointment', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'survey', ['Preliminary3'])

        # Adding M2M table for field have_disease on 'Preliminary3'
        m2m_table_name = db.shorten_name(u'survey_preliminary3_have_disease')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('preliminary3', models.ForeignKey(orm[u'survey.preliminary3'], null=False)),
            ('multipleselect', models.ForeignKey(orm[u'survey.multipleselect'], null=False))
        ))
        db.create_unique(m2m_table_name, ['preliminary3_id', 'multipleselect_id'])

        # Adding model 'Preliminary4'
        db.create_table(u'survey_preliminary4', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EmailUser'])),
            ('immediate_family', self.gf('django.db.models.fields.IntegerField')()),
            ('cancer_family', self.gf('django.db.models.fields.IntegerField')()),
            ('mother_alive', self.gf('django.db.models.fields.IntegerField')()),
            ('mother_old', self.gf('django.db.models.fields.IntegerField')()),
            ('mother_depend', self.gf('django.db.models.fields.IntegerField')()),
            ('mother_passed_old', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('father_alive', self.gf('django.db.models.fields.IntegerField')()),
            ('father_old', self.gf('django.db.models.fields.IntegerField')()),
            ('father_depend', self.gf('django.db.models.fields.IntegerField')()),
            ('father_passed_old', self.gf('django.db.models.fields.IntegerField')()),
            ('long_live', self.gf('django.db.models.fields.IntegerField')()),
            ('child_old', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'survey', ['Preliminary4'])

        # Adding M2M table for field mother_cause on 'Preliminary4'
        m2m_table_name = db.shorten_name(u'survey_preliminary4_mother_cause')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('preliminary4', models.ForeignKey(orm[u'survey.preliminary4'], null=False)),
            ('multipleselect', models.ForeignKey(orm[u'survey.multipleselect'], null=False))
        ))
        db.create_unique(m2m_table_name, ['preliminary4_id', 'multipleselect_id'])

        # Adding M2M table for field father_cause on 'Preliminary4'
        m2m_table_name = db.shorten_name(u'survey_preliminary4_father_cause')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('preliminary4', models.ForeignKey(orm[u'survey.preliminary4'], null=False)),
            ('multipleselect', models.ForeignKey(orm[u'survey.multipleselect'], null=False))
        ))
        db.create_unique(m2m_table_name, ['preliminary4_id', 'multipleselect_id'])

        # Adding M2M table for field family_history on 'Preliminary4'
        m2m_table_name = db.shorten_name(u'survey_preliminary4_family_history')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('preliminary4', models.ForeignKey(orm[u'survey.preliminary4'], null=False)),
            ('multipleselect', models.ForeignKey(orm[u'survey.multipleselect'], null=False))
        ))
        db.create_unique(m2m_table_name, ['preliminary4_id', 'multipleselect_id'])


    def backwards(self, orm):
        # Deleting model 'MultipleSelect'
        db.delete_table(u'survey_multipleselect')

        # Deleting model 'Preliminary1'
        db.delete_table(u'survey_preliminary1')

        # Removing M2M table for field source_of_stress on 'Preliminary1'
        db.delete_table(db.shorten_name(u'survey_preliminary1_source_of_stress'))

        # Deleting model 'Preliminary2'
        db.delete_table(u'survey_preliminary2')

        # Deleting model 'Preliminary3'
        db.delete_table(u'survey_preliminary3')

        # Removing M2M table for field have_disease on 'Preliminary3'
        db.delete_table(db.shorten_name(u'survey_preliminary3_have_disease'))

        # Deleting model 'Preliminary4'
        db.delete_table(u'survey_preliminary4')

        # Removing M2M table for field mother_cause on 'Preliminary4'
        db.delete_table(db.shorten_name(u'survey_preliminary4_mother_cause'))

        # Removing M2M table for field father_cause on 'Preliminary4'
        db.delete_table(db.shorten_name(u'survey_preliminary4_father_cause'))

        # Removing M2M table for field family_history on 'Preliminary4'
        db.delete_table(db.shorten_name(u'survey_preliminary4_family_history'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.emailuser': {
            'Meta': {'object_name': 'EmailUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'survey.multipleselect': {
            'Meta': {'object_name': 'MultipleSelect'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'option': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'survey.preliminary1': {
            'Meta': {'object_name': 'Preliminary1'},
            'brain_activity': ('django.db.models.fields.IntegerField', [], {}),
            'cope_stress': ('django.db.models.fields.IntegerField', [], {}),
            'current_work': ('django.db.models.fields.IntegerField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'formal_education': ('django.db.models.fields.IntegerField', [], {}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_person_contact': ('django.db.models.fields.IntegerField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'marital_status': ('django.db.models.fields.IntegerField', [], {}),
            'new_relation': ('django.db.models.fields.IntegerField', [], {}),
            'source_of_stress': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['survey.MultipleSelect']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EmailUser']"}),
            'work_hour': ('django.db.models.fields.IntegerField', [], {}),
            'work_week': ('django.db.models.fields.IntegerField', [], {})
        },
        u'survey.preliminary2': {
            'Meta': {'object_name': 'Preliminary2'},
            'air_pollution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aspirin': ('django.db.models.fields.IntegerField', [], {}),
            'body_mass_index': ('django.db.models.fields.IntegerField', [], {}),
            'coffee': ('django.db.models.fields.IntegerField', [], {}),
            'day_alcohol': ('django.db.models.fields.IntegerField', [], {}),
            'exposure_smoke': ('django.db.models.fields.IntegerField', [], {}),
            'floss_teeth': ('django.db.models.fields.IntegerField', [], {}),
            'glass_alcohol': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lung_disease': ('django.db.models.fields.IntegerField', [], {}),
            'many_smoke': ('django.db.models.fields.IntegerField', [], {}),
            'often_smoke': ('django.db.models.fields.IntegerField', [], {}),
            'seatbelt': ('django.db.models.fields.IntegerField', [], {}),
            'second_smoke': ('django.db.models.fields.IntegerField', [], {}),
            'sunscreen': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EmailUser']"})
        },
        u'survey.preliminary3': {
            'Meta': {'object_name': 'Preliminary3'},
            'bowel_movement': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'doctor_appointment': ('django.db.models.fields.IntegerField', [], {}),
            'have_disease': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'survey_multiple_2'", 'symmetrical': 'False', 'to': u"orm['survey.MultipleSelect']"}),
            'heart_attack': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skin_cancer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EmailUser']"})
        },
        u'survey.preliminary4': {
            'Meta': {'object_name': 'Preliminary4'},
            'cancer_family': ('django.db.models.fields.IntegerField', [], {}),
            'child_old': ('django.db.models.fields.IntegerField', [], {}),
            'family_history': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'survey_multiple_5'", 'symmetrical': 'False', 'to': u"orm['survey.MultipleSelect']"}),
            'father_alive': ('django.db.models.fields.IntegerField', [], {}),
            'father_cause': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'survey_multiple_4'", 'symmetrical': 'False', 'to': u"orm['survey.MultipleSelect']"}),
            'father_depend': ('django.db.models.fields.IntegerField', [], {}),
            'father_old': ('django.db.models.fields.IntegerField', [], {}),
            'father_passed_old': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immediate_family': ('django.db.models.fields.IntegerField', [], {}),
            'long_live': ('django.db.models.fields.IntegerField', [], {}),
            'mother_alive': ('django.db.models.fields.IntegerField', [], {}),
            'mother_cause': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'survey_multiple_3'", 'symmetrical': 'False', 'to': u"orm['survey.MultipleSelect']"}),
            'mother_depend': ('django.db.models.fields.IntegerField', [], {}),
            'mother_old': ('django.db.models.fields.IntegerField', [], {}),
            'mother_passed_old': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EmailUser']"})
        }
    }

    complete_apps = ['survey']