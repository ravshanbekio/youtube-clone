# Generated by Django 4.0.3 on 2022-05-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='recommended_channels',
            field=models.ManyToManyField(blank=True, to='base.channel'),
        ),
    ]
