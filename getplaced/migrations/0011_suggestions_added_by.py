# Generated by Django 3.1.1 on 2020-11-13 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('getplaced', '0010_auto_20201113_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='added_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]