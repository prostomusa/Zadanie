# Generated by Django 2.2.2 on 2020-10-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0002_auto_20201029_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='number_of_passport',
            field=models.IntegerField(unique=True, verbose_name='Серия и номер паспорта'),
        ),
    ]
