from typing import Any, Callable, Dict, Optional

from django.db.models import Model
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from django_oapif.mixins import OAPIFDescribeModelViewSetMixin
from django_oapif.urls import oapif_router

from .filters import BboxFilterBackend


def register_oapif_viewset(
    key: Optional[str] = None,
    skip_geom: Optional[bool] = False,
    custom_serializer_attrs: Dict[str, Any] = None,
    custom_viewset_attrs: Dict[str, Any] = None,
) -> Callable[[Any], Model]:
    """
    This decorator takes care of all boilerplate code (creating a serializer, a viewset and registering it) to register
    a model to the default OAPIF endpoint.

    - key: allows to pass a custom name for the collection (defaults to the model's label)
    - custom_serializer_attrs: allows to pass custom attributes to set to the serializer's Meta (e.g. custom fields)
    - custom_viewset_attrs: allows to pass custom attributes to set to the viewset (e.g. custom pagination class)
    """

    if custom_serializer_attrs is None:
        custom_serializer_attrs = {}

    if custom_viewset_attrs is None:
        custom_viewset_attrs = {}

    def inner(Model):
        """
        Create the serializers
        1 for viewsets for models with a geometry and
        1 for viewsets for models without (aka 'non-geometric features').
        """

        class AutoSerializer(GeoFeatureModelSerializer):
            class Meta:
                model = Model
                fields = "__all__"
                geo_field = "geom"

        class AutoNoGeomSerializer(ModelSerializer):
            class Meta:
                mode = Model
                fields = "__all__"

        if skip_geom:
            viewset_serializer_class = AutoNoGeomSerializer
            viewset_oapif_geom_lookup = None
        else:
            viewset_serializer_class = AutoSerializer
            viewset_oapif_geom_lookup = "geom"  # one day this will be retrieved automatically from the serializer

        # Create the viewset
        class Viewset(OAPIFDescribeModelViewSetMixin, viewsets.ModelViewSet):
            queryset = Model.objects.all()
            serializer_class = viewset_serializer_class

            # TODO: these should probably be moved to the mixin
            oapif_title = Model._meta.verbose_name
            oapif_description = Model.__doc__

            # (one day this will be retrieved automatically from the serializer)
            oapif_geom_lookup = viewset_oapif_geom_lookup
            filter_backends = [BboxFilterBackend]

        # Apply custom serializer attributes
        if viewset_serializer_class.__name__ == "AutoNoGeomSerializer":
            for k, v in custom_serializer_attrs.items():
                setattr(AutoNoGeomSerializer.Meta, k, v)

        elif viewset_serializer_class.__name__ == "AutoSerializer":
            for k, v in custom_serializer_attrs.items():
                setattr(AutoSerializer.Meta, k, v)

        # Apply custom viewset attributes
        for k, v in custom_viewset_attrs.items():
            setattr(Viewset, k, v)

        # Register the model
        oapif_router.register(
            key or Model._meta.label_lower, Viewset, key or Model._meta.label_lower
        )

        return Model

    return inner
