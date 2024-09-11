# Generated by Django 5.1 on 2024-09-11 05:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0033_alter_arivaltable_agency_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='arivaltable',
            name='currency_rate',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyfullkyc',
            name='kyc_status',
            field=models.BooleanField(default=False),
        ),
    ]
