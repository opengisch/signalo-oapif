# Generated by Django 4.2.6 on 2023-10-14 12:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line_2056_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Line_2056_10fields_local_geom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoGeom_100fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_10', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_11', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_12', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_13', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_14', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_15', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_16', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_17', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_18', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_19', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_20', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_21', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_22', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_23', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_24', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_25', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_26', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_27', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_28', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_29', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_30', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_31', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_32', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_33', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_34', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_35', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_36', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_37', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_38', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_39', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_40', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_41', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_42', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_43', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_44', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_45', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_46', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_47', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_48', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_49', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_50', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_51', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_52', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_53', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_54', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_55', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_56', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_57', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_58', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_59', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_60', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_61', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_62', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_63', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_64', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_65', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_66', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_67', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_68', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_69', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_70', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_71', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_72', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_73', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_74', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_75', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_76', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_77', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_78', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_79', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_80', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_81', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_82', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_83', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_84', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_85', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_86', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_87', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_88', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_89', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('field_90', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_91', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_92', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_93', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_94', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_95', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_96', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_97', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_98', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_99', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoGeom_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Point_2056_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Point_2056_10fields_local_geom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Polygon_2056_10fields',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2056, verbose_name='Geometry')),
            ],
        ),
        migrations.CreateModel(
            name='Polygon_2056_10fields_local_geom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2056, verbose_name='Geometry')),
            ],
        ),
        migrations.CreateModel(
            name='SecretLayer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('field_0', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 0')),
                ('field_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 1')),
                ('field_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 2')),
                ('field_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 3')),
                ('field_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 4')),
                ('field_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 5')),
                ('field_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 6')),
                ('field_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 7')),
                ('field_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 8')),
                ('field_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='Field 9')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=2056, verbose_name='Geometry')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
