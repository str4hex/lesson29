# Generated by Django 4.1.2 on 2022-11-19 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ad_description_alter_ad_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='Id',
            new_name='id',
        ),
    ]
