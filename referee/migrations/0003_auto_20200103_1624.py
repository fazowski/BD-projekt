# Generated by Django 3.0 on 2020-01-03 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referee', '0002_auto_20200103_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchstatus',
            options={'verbose_name': 'Status meczu', 'verbose_name_plural': 'Statusy meczy'},
        ),
    ]
