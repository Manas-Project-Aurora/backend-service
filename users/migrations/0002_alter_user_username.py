# Generated by Django 5.1.6 on 2025-04-12 18:47

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=users.models.default_username, max_length=150, unique=True),
        ),
    ]
