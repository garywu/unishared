# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('website_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('website', ['Country'])

        # Adding model 'Organization'
        db.create_table('website_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Country'], null=True)),
            ('members_role', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('website', ['Organization'])

        # Adding model 'Field'
        db.create_table('website_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('website', ['Field'])

        # Adding model 'Training'
        db.create_table('website_training', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('resource_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_live', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_displayed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator', to=orm['auth.User'])),
        ))
        db.send_create_signal('website', ['Training'])

        # Adding M2M table for field cowriters on 'Training'
        db.create_table('website_training_cowriters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm['website.training'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('website_training_cowriters', ['training_id', 'user_id'])

        # Adding M2M table for field participants on 'Training'
        db.create_table('website_training_participants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('training', models.ForeignKey(orm['website.training'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('website_training_participants', ['training_id', 'user_id'])

        # Adding model 'TrainingTempShare'
        db.create_table('website_trainingtempshare', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Training'])),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')(null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
        ))
        db.send_create_signal('website', ['TrainingTempShare'])

        # Adding model 'TrainingSchedule'
        db.create_table('website_trainingschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Training'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_scheduled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('website', ['TrainingSchedule'])

        # Adding model 'TrainingParticipation'
        db.create_table('website_trainingparticipation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('training', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Training'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('website', ['TrainingParticipation'])

        # Adding model 'UserProfile'
        db.create_table('website_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Field'], null=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Organization'], null=True)),
            ('is_organization_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isUniStar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_student', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('about_me', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('facebook_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('facebook_profile_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('twitter_profile_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('linkedin_profile_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('website_url', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=255, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('raw_data', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('website', ['UserProfile'])

        # Adding model 'PublicProfilePermissions'
        db.create_table('website_publicprofilepermissions', (
            ('public_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_user', primary_key=True, to=orm['auth.User'])),
            ('allowed_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='allowed_user', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('website', ['PublicProfilePermissions'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('website_country')

        # Deleting model 'Organization'
        db.delete_table('website_organization')

        # Deleting model 'Field'
        db.delete_table('website_field')

        # Deleting model 'Training'
        db.delete_table('website_training')

        # Removing M2M table for field cowriters on 'Training'
        db.delete_table('website_training_cowriters')

        # Removing M2M table for field participants on 'Training'
        db.delete_table('website_training_participants')

        # Deleting model 'TrainingTempShare'
        db.delete_table('website_trainingtempshare')

        # Deleting model 'TrainingSchedule'
        db.delete_table('website_trainingschedule')

        # Deleting model 'TrainingParticipation'
        db.delete_table('website_trainingparticipation')

        # Deleting model 'UserProfile'
        db.delete_table('website_userprofile')

        # Deleting model 'PublicProfilePermissions'
        db.delete_table('website_publicprofilepermissions')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'website.field': {
            'Meta': {'object_name': 'Field'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'website.organization': {
            'Meta': {'object_name': 'Organization'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members_role': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.publicprofilepermissions': {
            'Meta': {'object_name': 'PublicProfilePermissions'},
            'allowed_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allowed_user'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'public_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_user'", 'primary_key': 'True', 'to': "orm['auth.User']"})
        },
        'website.training': {
            'Meta': {'object_name': 'Training'},
            'cowriters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cowriters'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_displayed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'participants'", 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'resource_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'website.trainingparticipation': {
            'Meta': {'object_name': 'TrainingParticipation'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Training']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'website.trainingschedule': {
            'Meta': {'object_name': 'TrainingSchedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_scheduled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Training']"})
        },
        'website.trainingtempshare': {
            'Meta': {'object_name': 'TrainingTempShare'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'training': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Training']"})
        },
        'website.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'access_token': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Field']", 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'isUniStar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_organization_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_student': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'linkedin_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Organization']", 'null': 'True'}),
            'raw_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'twitter_profile_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website_url': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['website']