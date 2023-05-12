# Generated by Django 4.2 on 2023-05-12 14:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models

import signalo.value_lists.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialSignType',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('active', models.BooleanField(default=True)),
                ('value_de', models.CharField(blank=True, max_length=255, null=True)),
                ('value_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('value_it', models.CharField(blank=True, max_length=255, null=True)),
                ('value_ro', models.CharField(blank=True, max_length=255, null=True)),
                ('description_de', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('description_it', models.TextField(blank=True, null=True)),
                ('description_ro', models.TextField(blank=True, null=True)),
                ('img_de', models.FileField(storage=signalo.value_lists.models.SignsFileSystemStorage(location='/media_volume/official_signs'), upload_to='')),
                ('img_fr', models.FileField(storage=signalo.value_lists.models.SignsFileSystemStorage(location='/media_volume/official_signs'), upload_to='')),
                ('img_it', models.FileField(storage=signalo.value_lists.models.SignsFileSystemStorage(location='/media_volume/official_signs'), upload_to='')),
                ('img_ro', models.FileField(storage=signalo.value_lists.models.SignsFileSystemStorage(location='/media_volume/official_signs'), upload_to='')),
                ('img_height', models.IntegerField(default=0)),
                ('img_width', models.IntegerField(default=0)),
                ('no_dynamic_inscription', models.IntegerField(default=0)),
                ('default_inscription1', models.CharField(blank=True, max_length=255, null=True)),
                ('default_inscription2', models.CharField(blank=True, max_length=255, null=True)),
                ('default_inscription3', models.CharField(blank=True, max_length=255, null=True)),
                ('default_inscription4', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
