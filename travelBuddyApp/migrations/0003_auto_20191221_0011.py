# Generated by Django 2.2 on 2019-12-21 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelBuddyApp', '0002_travel_isjoined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='desc',
            new_name='dest',
        ),
    ]
