# Generated by Django 5.0.1 on 2024-01-20 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_examplemodel_date_field_examplemodel_date_time_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examplemodel',
            name='duration_field',
        ),
    ]