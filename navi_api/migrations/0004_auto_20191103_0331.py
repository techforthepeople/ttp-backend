# Generated by Django 2.2.6 on 2019-11-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navi_api', '0003_auto_20191103_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuslog',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='statuslog',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
    ]
