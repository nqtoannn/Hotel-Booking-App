# Generated by Django 4.2.5 on 2023-10-23 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_userpreferences_city_userpreferences_updateat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreferences',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='updateAt',
        ),
    ]
