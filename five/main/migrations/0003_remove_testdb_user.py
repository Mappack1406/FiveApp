# Generated by Django 4.0.5 on 2022-07-06 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_testdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testdb',
            name='user',
        ),
    ]