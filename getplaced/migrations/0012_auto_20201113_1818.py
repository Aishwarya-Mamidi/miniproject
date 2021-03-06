# Generated by Django 3.1.1 on 2020-11-13 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getplaced', '0011_suggestions_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement_history',
            name='package',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placement_history',
            name='ptype',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='placement_history',
            name='pyear',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
