# Generated by Django 2.1.2 on 2018-10-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileindex', '0002_auto_20181020_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labbook',
            name='e_copy',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='relatedfile',
            name='e_copy',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='e_copy',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='studyplan',
            name='e_copy',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]