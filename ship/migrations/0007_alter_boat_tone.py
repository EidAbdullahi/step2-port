# Generated by Django 3.2.9 on 2021-11-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0006_auto_20211130_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='tone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
