# Generated by Django 3.2.9 on 2021-12-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0018_alter_container_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='boat_docs',
            field=models.FileField(blank=True, null=True, upload_to='BoatDocuments/'),
        ),
        migrations.AddField(
            model_name='ship',
            name='ship_docs',
            field=models.FileField(blank=True, null=True, upload_to='ShipDocuments/'),
        ),
    ]