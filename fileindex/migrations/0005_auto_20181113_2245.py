# Generated by Django 2.1.2 on 2018-11-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileindex', '0004_auto_20181113_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyplan',
            name='status',
            field=models.CharField(choices=[('PEN', 'Pendinng'), ('IND', 'In draft'), ('COM', 'Complete')], default='PEN', max_length=3),
        ),
    ]