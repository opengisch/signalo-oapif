from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import Client
from rest_framework.test import APITestCase

from .models import (
    TestPermissionAllowAny,
    TestPermissionDefaultPermissionsSettings,
    TestPermissionIsAdminUserModel,
)

app_collections_url = "/oapif/collections"
app_models_url = f"{app_collections_url}/signalo_edge_cases"


class Url(str, Enum):
    allow_any = f"{app_models_url}.{TestPermissionAllowAny.__name__.lower()}"
    default = (
        f"{app_models_url}.{TestPermissionDefaultPermissionsSettings.__name__.lower()}"
    )
    is_admin = f"{app_models_url}.{TestPermissionIsAdminUserModel.__name__.lower()}"
    list = f"{app_collections_url}"


class Crud(str, Enum):
    create = "create"
    list = "list"
    read = "read"
    partial_update = "partial_update"
    update = "update"
    destroy = "destroy"


class Roles(str, Enum):
    anonymous = "anonymous"
    no_specific = "no_specific"
    model_specific = "model_specific"
    readonly = "readonly"
    all_perms = "all_perms"
    admin = "admin"


status_codes_matrix = {
    Roles.anonymous: {
        Url.allow_any: {
            Crud.create: 201,
            Crud.list: 200,
            Crud.read: 200,
            Crud.partial_update: 200,
            Crud.update: 200,
            Crud.destroy: 204,
        },
        Url.default: {
            Crud.create: 403,
            Crud.list: 200,
            Crud.read: 200,
            Crud.partial_update: 403,
            Crud.update: 403,
            Crud.destroy: 403,
        },
        Url.is_admin: {
            Crud.create: 403,
            Crud.list: 403,
            Crud.read: 403,
            Crud.partial_update: 403,
            Crud.update: 403,
            Crud.destroy: 403,
        },
        Url.list: {"list": 200},
    },
    Roles.admin: {
        Url.allow_any: {
            Crud.create: 201,
            Crud.list: 200,
            Crud.read: 200,
            Crud.partial_update: 200,
            Crud.update: 200,
            Crud.destroy: 204,
        },
        Url.default: {
            Crud.create: 201,
            Crud.list: 200,
            Crud.read: 200,
            Crud.partial_update: 200,
            Crud.update: 200,
            Crud.destroy: 204,
        },
        Url.is_admin: {
            Crud.create: 201,
            Crud.list: 200,
            Crud.read: 200,
            Crud.partial_update: 200,
            Crud.update: 200,
            Crud.destroy: 204,
        },
        Url.list: {"list": 200},
        # Roles.no_specific: "todo",
        # Roles.model_specific: "todo",
        # Roles.readonly: "todo",
        # Roles.all_perms: "todo",
    },
}


def extract_ids_from_items(contents: Dict[str, Any]) -> List[str]:
    return [feature["id"] for feature in contents["features"]]


def make_request(client: Client, crud_type: Crud, url: str) -> Tuple[str, int, Any]:
    items_url = f"{url}/items"
    params = {"geom": "Point(2600000 1200000)"}
    data = {"geom": "Point(1300000 600000)"}

    if crud_type == Crud.create:
        resp = client.post(items_url, data, format="json")
        return (items_url, resp.status_code, None)

    if crud_type == Crud.list:
        collections_or_items = url if url == app_collections_url else items_url
        resp = client.get(collections_or_items, params, format="json")
        return (collections_or_items, resp.status_code, resp.json())

    if crud_type == Crud.read:
        resp = client.get(items_url, params, format="json")
        return (items_url, resp.status_code, resp.json())

    items = client.get(items_url, format="json").json()
    feature_ids = extract_ids_from_items(items)
    single_item_id = feature_ids[0]
    detail_url = f"{items_url}/{single_item_id}"

    if crud_type == Crud.partial_update:
        resp = client.patch(detail_url, data, format="json")
        return (detail_url, resp.status_code, None)

    if crud_type == Crud.update:
        resp = client.put(detail_url, data, format="json")
        return (detail_url, resp.status_code, None)

    if crud_type == Crud.destroy:
        resp = client.delete(detail_url, format="json")
        return (detail_url, resp.status_code, None)

    raise TypeError(f"Not supported CRUD type: {crud_type}")


def traverse_matrix(
    client: Client,
    role: Roles,
    endpoint: Optional[str] = None,
    to_filter_out: Optional[list[str]] = None,
) -> Tuple[int, List[str]]:
    failed = []
    tot = 0
    for crud_name, expected_status_code in status_codes_matrix[role][endpoint].items():
        actual_url, response_code, results = make_request(client, crud_name, endpoint)

        if response_code != expected_status_code:
            failed.append(
                f"{crud_name}: {actual_url} (got {response_code}, expected {expected_status_code})"
            )

        if actual_url == app_collections_url:
            collection_ids = {collection["id"] for collection in results["collections"]}

            if collection_ids.intersection(to_filter_out):
                failed.append(f"{actual_url} unable to filter out: {to_filter_out}")

        tot += 1

    print(
        f"{role} traversed {endpoint}. To filter out: {len(to_filter_out) if to_filter_out else 0}"
    )
    return (tot, failed)


class TestViewsets(APITestCase):
    def setUp(self):
        # Test data
        call_command("populate_edge_cases")
        # Admin user to authenticate some requests
        self.admin_user = User.objects.create_user(
            username="username",
            password="password",
            is_staff=True,
        )

    def tearDown(self):
        self.client.force_authenticate(user=None)

    # pre-tests

    def test_objects_domain(self):
        allow_any = TestPermissionAllowAny.objects.all().count()
        default_settings = (
            TestPermissionDefaultPermissionsSettings.objects.all().count()
        )
        admin_user = TestPermissionIsAdminUserModel.objects.all().count()
        self.assertGreater(allow_any, 0)
        self.assertGreater(default_settings, 0)
        self.assertGreater(admin_user, 0)

    # Anonymous

    def test_anonymous_versus_any(self):
        tot, failed = traverse_matrix(self.client, Roles.anonymous, Url.allow_any)

        if failed:
            print(f" => Failed {len(failed)}/{tot}")
            print("\n".join(failed))

        self.assertTrue(not failed)

    def test_anonymous_versus_default_permissions(self):
        tot, failed = traverse_matrix(self.client, Roles.anonymous, Url.default)

        if failed:
            print(f" => Failed {len(failed)}/{tot}")
            print("\n".join(failed))

        self.assertTrue(not failed)

    def test_anonymous_versus_is_admin(self):
        tot, failed = traverse_matrix(self.client, Roles.anonymous, Url.is_admin)

        if failed:
            print(f" => Failed {len(failed)}/{tot}")
            print("\n".join(failed))

        self.assertTrue(not failed)

    # # Admin

    # def test_admin_versus_any(self):
    #     self.client.force_authenticate(user=self.admin_user)

    #     model = TestPermissionAllowAny
    #     path = f"{app_models_url}.{model.__name__.lower()}"
    #     tot, failed = traverse_matrix(self.client, Roles.anonymous, path)

    #     if failed:
    #         print(f" => Failed {len(failed)}/{tot}")
    #         print("\n".join(failed))

    #     self.assertTrue(not failed)

    # def test_admin_versus_default_permissions(self):
    #     self.client.force_authenticate(user=self.admin_user)

    #     model = TestPermissionDefaultPermissionsSettings
    #     path = f"{app_models_url}.{model.__name__.lower()}"
    #     tot, failed = traverse_matrix(self.client, Roles.anonymous, path)

    #     if failed:
    #         print(f" => Failed {len(failed)}/{tot}")
    #         print("\n".join(failed))

    #     self.assertTrue(not failed)

    # def test_admin_versus_is_admin(self):
    #     self.client.force_authenticate(user=self.admin_user)

    #     model = TestPermissionIsAdminUserModel
    #     path = f"{app_models_url}.{model.__name__.lower()}"
    #     tot, failed = traverse_matrix(self.client, Roles.anonymous, path)

    #     if failed:
    #         print(f" => Failed {len(failed)}/{tot}")
    #         print("\n".join(failed))

    #     self.assertTrue(not failed)
