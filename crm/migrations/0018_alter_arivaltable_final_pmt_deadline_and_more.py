# Generated by Django 5.0.4 on 2024-07-31 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_alter_arivaltable_staff_arivaltable_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arivaltable',
            name='final_pmt_deadline',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='gurantee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.gurantee'),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='inv_amount',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='itinerary_submit_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='payment_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.paymentstatus'),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='visa_letter_submit_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='arivaltable',
            name='voucher_submit_date',
            field=models.DateField(blank=True),
        ),
    ]
