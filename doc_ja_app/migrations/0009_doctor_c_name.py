# Generated by Django 4.2.11 on 2024-04-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_ja_app', '0008_alter_doctor_c_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_c',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
