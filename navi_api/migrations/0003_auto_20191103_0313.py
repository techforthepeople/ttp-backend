# Generated by Django 2.2.6 on 2019-11-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi_api', '0002_statuslog_pressure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emtprofile',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]