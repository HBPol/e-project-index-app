# Generated by Django 2.1.2 on 2018-10-14 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docindex', '0006_auto_20181014_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labbook',
            name='doc_type',
        ),
        migrations.RemoveField(
            model_name='relatedfile',
            name='doc_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='doc_type',
        ),
        migrations.RemoveField(
            model_name='studyplan',
            name='doc_type',
        ),
        migrations.AddField(
            model_name='labbook',
            name='document_code',
            field=models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='relatedfile',
            name='document_code',
            field=models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='report',
            name='document_code',
            field=models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='studyplan',
            name='document_code',
            field=models.CharField(choices=[('SP', 'Study plan'), ('R', 'Report'), ('RDF', 'Related file'), ('LBN', 'Lab book')], default='', max_length=3),
        ),
        migrations.DeleteModel(
            name='DocumentType',
        ),
    ]