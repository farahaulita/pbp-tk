# Generated by Django 3.2.7 on 2021-11-05 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_viewer', '0002_auto_20211104_2237'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Submission',
        ),
        migrations.RemoveField(
            model_name='task',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]