# Generated by Django 4.2.11 on 2024-05-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_ja_app', '0011_remove_reservation_from_remove_reservation_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='expert',
            field=models.CharField(choices=[('پزشک عمومی', 'پزشک عمومی'), ('متخصص زیبایی', 'متخصص زیبایی'), ('متخصص قلب', 'متخصص قلب'), ('متخصص غدد', 'متخصص غدد'), ('متخصص زنان', 'متخصص زنان'), ('متخصص داخلی', 'متخصص داخلی'), ('متخصص گوش،حلق،بینی', 'متخصص گوش،حلق،بینی'), ('متخصص داخلی', 'متخصص داخلی'), ('جراخ پلاستیک', 'جراخ پلاستیک'), ('متخصص اطفال', 'متخصص اطفال'), ('متخصص مامایی', 'متخصص مامایی'), ('متخصص مغز و اعصاب', 'متخصص مغز و اعصاب'), ('دندانپزشک', 'دندانپزشک')], max_length=120),
        ),
    ]
