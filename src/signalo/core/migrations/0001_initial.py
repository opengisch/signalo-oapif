# Generated by Django 4.2 on 2023-04-27 08:28

import uuid

import computedfields.resolver
import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signalo_vl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Azimuth',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.SmallIntegerField(default=0)),
                ('geom', django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056, verbose_name='Geometry')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('_serialized', models.CharField(editable=False, max_length=1000, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=2056, verbose_name='Geometry')),
                ('azimuth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signs', to='signalo_core.azimuth')),
                ('sign_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='official_sign', to='signalo_vl.officialsigntype')),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.AddField(
            model_name='azimuth',
            name='pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='azimuths', to='signalo_core.pole'),
        ),
    ]
