# Generated by Django 3.2.7 on 2021-09-21 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_leve_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='subcategory_id',
        ),
    ]
