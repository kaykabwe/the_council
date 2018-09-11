# Generated by Django 2.0.4 on 2018-08-31 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0021_auto_20180831_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='district_latitude',
            field=models.CharField(blank=True, help_text='Use decimal degrees format(ie: -28.32282)', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='district_longitude',
            field=models.CharField(blank=True, help_text='Use decimal degrees format(ie: 28.32282)', max_length=20, null=True),
        ),
    ]
