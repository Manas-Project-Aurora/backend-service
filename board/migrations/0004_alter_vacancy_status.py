# Generated by Django 5.2 on 2025-04-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_organizationcontact_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('suspended', 'Suspended'), ('rejected', 'Rejected')], max_length=255),
        ),
    ]
