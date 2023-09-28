# Generated by Django 4.2.5 on 2023-09-28 20:38

import uuid

import computedfields.resolver
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line_2056_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=2056, verbose_name='Geometry')),
                ('field_0', models.CharField(max_length=255, verbose_name='Field 0')),
                ('field_1', models.CharField(max_length=255, verbose_name='Field 1')),
                ('field_2', models.CharField(max_length=255, verbose_name='Field 2')),
                ('field_3', models.CharField(max_length=255, verbose_name='Field 3')),
                ('field_4', models.CharField(max_length=255, verbose_name='Field 4')),
                ('field_5', models.CharField(max_length=255, verbose_name='Field 5')),
                ('field_6', models.CharField(max_length=255, verbose_name='Field 6')),
                ('field_7', models.CharField(max_length=255, verbose_name='Field 7')),
                ('field_8', models.CharField(max_length=255, verbose_name='Field 8')),
                ('field_9', models.CharField(max_length=255, verbose_name='Field 9')),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='NoGeom_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(max_length=255, verbose_name='Field 0')),
                ('field_1', models.CharField(max_length=255, verbose_name='Field 1')),
                ('field_2', models.CharField(max_length=255, verbose_name='Field 2')),
                ('field_3', models.CharField(max_length=255, verbose_name='Field 3')),
                ('field_4', models.CharField(max_length=255, verbose_name='Field 4')),
                ('field_5', models.CharField(max_length=255, verbose_name='Field 5')),
                ('field_6', models.CharField(max_length=255, verbose_name='Field 6')),
                ('field_7', models.CharField(max_length=255, verbose_name='Field 7')),
                ('field_8', models.CharField(max_length=255, verbose_name='Field 8')),
                ('field_9', models.CharField(max_length=255, verbose_name='Field 9')),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='Point_2056_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056, verbose_name='Geometry')),
                ('field_0', models.CharField(max_length=255, verbose_name='Field 0')),
                ('field_1', models.CharField(max_length=255, verbose_name='Field 1')),
                ('field_2', models.CharField(max_length=255, verbose_name='Field 2')),
                ('field_3', models.CharField(max_length=255, verbose_name='Field 3')),
                ('field_4', models.CharField(max_length=255, verbose_name='Field 4')),
                ('field_5', models.CharField(max_length=255, verbose_name='Field 5')),
                ('field_6', models.CharField(max_length=255, verbose_name='Field 6')),
                ('field_7', models.CharField(max_length=255, verbose_name='Field 7')),
                ('field_8', models.CharField(max_length=255, verbose_name='Field 8')),
                ('field_9', models.CharField(max_length=255, verbose_name='Field 9')),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
    ]
