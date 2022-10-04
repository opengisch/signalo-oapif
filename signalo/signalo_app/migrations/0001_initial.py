# Generated by Django 4.1.2 on 2022-10-04 15:56

import uuid

import computedfields.resolver
import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pole",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=2056, verbose_name="Geometry"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
            ],
            options={
                "abstract": False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name="Sign",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("order", models.IntegerField(default=1)),
                (
                    "computed_geom",
                    django.contrib.gis.db.models.fields.PointField(
                        editable=False, srid=2056, verbose_name="Geometry"
                    ),
                ),
                (
                    "pole",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="signs",
                        to="signalo_app.pole",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
    ]
