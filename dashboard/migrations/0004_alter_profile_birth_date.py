# Generated by Django 3.2.8 on 2021-11-05 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 11, 5)),
        ),
    ]