#!/usr/bin/env bash
mkdir django-ogcapif
cp -r src/django_oapif django-ogcapif/django_ogcapif/
cp MANIFEST.in pyproject.toml LICENSE README.md requirements.txt requirements-dev.txt django-ogcapif/
