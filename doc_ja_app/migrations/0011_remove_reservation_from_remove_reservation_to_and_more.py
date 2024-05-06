# Generated by Django 4.2.11 on 2024-04-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_ja_app', '0010_remove_hour_day_remove_reservation_hour_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='From',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='to',
        ),
        migrations.AddField(
            model_name='reservation',
            name='hour',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
