# Generated by Django 3.2.9 on 2021-12-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0014_auto_20211203_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Free', 'Free')], default='Pending', max_length=200),
        ),
    ]
