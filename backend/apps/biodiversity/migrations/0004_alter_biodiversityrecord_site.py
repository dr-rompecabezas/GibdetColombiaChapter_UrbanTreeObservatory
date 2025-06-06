# Generated by Django 5.1.7 on 2025-04-28 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversity', '0003_biodiversityrecord_neighborhood'),
        ('places', '0013_site_unique_site_per_zone_subzone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodiversityrecord',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='biodiversity_records', to='places.site', verbose_name='site'),
        ),
    ]
