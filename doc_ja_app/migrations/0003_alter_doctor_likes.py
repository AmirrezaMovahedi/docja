# Generated by Django 4.2.11 on 2024-04-12 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doc_ja_app', '0002_doctor_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='doctor_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
