# Generated by Django 5.1 on 2024-09-11 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_alter_contacttable_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arivaltable',
            old_name='final_pmt_amt',
            new_name='amt_recev',
        ),
        migrations.RemoveField(
            model_name='arivaltable',
            name='part_pmt_amt',
        ),
        migrations.RemoveField(
            model_name='arivaltable',
            name='part_pmt_deadline',
        ),
    ]
