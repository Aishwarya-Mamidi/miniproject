# Generated by Django 3.1.1 on 2020-11-16 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getplaced', '0019_sprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprofile',
            name='usern',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
