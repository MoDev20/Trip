# Generated by Django 2.2 on 2019-12-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelBuddyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='isJoined',
            field=models.BooleanField(default=False),
        ),
    ]
