# Generated by Django 3.1.1 on 2020-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getplaced', '0022_auto_20201121_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprofile',
            name='abt',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sprofile',
            name='prjdesc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sprofile',
            name='skl',
            field=models.TextField(),
        ),
    ]
