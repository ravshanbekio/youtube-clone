# Generated by Django 4.0.3 on 2022-05-28 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('main_image', models.URLField(blank=True, null=True)),
                ('banner', models.URLField(blank=True, null=True)),
                ('views', models.PositiveIntegerField(default=1)),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
                ('recommended_channels', models.ManyToManyField(default='No recommended channels', to='base.channel')),
            ],
        ),
    ]