# Generated by Django 5.1 on 2024-09-06 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0028_alter_staffdetails_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttable',
            name='contact_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.state'),
        ),
    ]
