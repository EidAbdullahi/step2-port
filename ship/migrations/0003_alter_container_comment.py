# Generated by Django 3.2.9 on 2021-11-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0002_alter_container_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='comment',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
