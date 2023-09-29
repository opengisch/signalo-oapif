from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = "Populate db with groups, set permissions, add users"

    @transaction.atomic
    def handle(self, *args, **options):
        """Populate db with groups, set permissions, add users"""
        adding = []
        modifying = []
        viewing = []

        for model in ("point_2056_10fields", "nogeom_10fields", "line_2056_10fields"):
            adding.append(Permission.objects.get(codename=f"add_{model}"))
            modifying.append(Permission.objects.get(codename=f"change_{model}"))
            viewing.append(Permission.objects.get(codename=f"view_{model}"))

        editing = adding + modifying + viewing

        editors, _ = Group.objects.get_or_create(name="editors")
        viewers, _ = Group.objects.get_or_create(name="viewers")
        viewers_wo_lines, _ = Group.objects.get_or_create(name="viewers_without_lines")

        editors.save()
        viewers.save()

        editors.permissions.set(editing)
        viewers.permissions.set(viewing)

        viewer, _ = User.objects.get_or_create(username="demo_viewer")
        viewer_wo_lines, _ = User.objects.get_or_create(username="demo_viewer_without_lines")
        editor, _ = User.objects.get_or_create(username="demo_editor")
        super_user = User.objects.create_superuser(username="admin", is_staff=True)

        for user in (viewer, viewer_wo_lines, editor, super_user):
            user.set_password("123")
            user.save()

        editor.groups.add(editors)
        viewer.groups.add(viewers)
        viewer_wo_lines.groups.add(viewers_wo_lines)

        print(
            f"👥 added users 'demo_editor' & 'demo_viewer' to group 'editors' and 'viewers' respectively. Permissions set accordingly."
        )
