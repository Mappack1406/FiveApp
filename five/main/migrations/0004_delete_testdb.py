# Generated by Django 4.0.5 on 2022-07-06 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_testdb_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testdb',
        ),
    ]
