# Generated by Django 5.0.3 on 2024-04-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_alter_event_date_alter_event_time_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
