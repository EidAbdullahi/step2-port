# Generated by Django 3.2.9 on 2021-12-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0016_alter_container_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='price',
            field=models.FloatField(choices=[('112.5', '112.5'), ('62', '62')], default='112.5'),
        ),
    ]
